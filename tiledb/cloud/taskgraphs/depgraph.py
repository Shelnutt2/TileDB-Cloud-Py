"""Common internal-only types and tools."""

import collections
from typing import Deque, Dict, FrozenSet, Generic, Iterable, List, Set, Tuple, TypeVar

_T = TypeVar("_T")


class DepGraph(Generic[_T]):
    """A directed dependency graph which forbids cycles."""

    def __init__(self):
        self._parent_to_children: Dict[_T, Set[_T]] = {}
        """A mapping from parent to children, i.e. parents come before child."""
        self._child_to_parents: Dict[_T, Set[_T]] = {}
        """A mapping from child to parents, i.e. child comes after parents."""
        self._topo_sorted: List[_T] = []
        """A topologically-sorted list of nodes."""

    @property
    def topo_sorted(self) -> Tuple[_T, ...]:
        """A topologically-sorted view of the dependency graph."""
        return tuple(self._topo_sorted)

    def add_new_node(self, child: _T, parents: Iterable[_T]) -> None:
        """Adds a new child to the graph, where all parents exist."""
        if child in self._parent_to_children:
            raise KeyError(f"{child!r} is already in the graph.")
        parent_set = set(parents)
        if child in parent_set:
            raise CyclicGraphError(f"{child!r} can't be its own parent.")
        missing_keys = parent_set - self._parent_to_children.keys()
        if missing_keys:
            raise KeyError(f"Entries {missing_keys!r} are not in the graph.")
        # This isn't a no-op -- it ensures that the child node exists in both
        # our mappings.
        self._parent_to_children[child] = set()
        self._child_to_parents[child] = set()
        # When adding a completely new node to a DAG, you can't get a cycle.
        for parent in parents:
            self._add_edge_unsafe(child=child, parent=parent)
        self._topo_sorted.append(child)

    def add_edge(self, *, child: _T, parent: _T) -> None:
        """Adds a new edge between two existing nodes."""
        if child not in self._parent_to_children:
            raise KeyError(f"{child!r} is not part of the graph")
        if parent not in self._parent_to_children:
            raise KeyError(f"{parent!r} is not part of the graph")
        self._add_edge_unsafe(child=child, parent=parent)
        try:
            self._topo_sorted = self._topo_sort()
        except CyclicGraphError:
            self._remove_edge(child=child, parent=parent)
            raise

    def remove(self, node: _T) -> None:
        """Removes a node, and all its connections, from the network."""
        if node not in self._parent_to_children:
            raise KeyError(f"{node!r} is not part of the graph")
        for child in self._parent_to_children[node]:
            self._child_to_parents[child].remove(node)
        del self._parent_to_children[node]
        for parent in self._child_to_parents[node]:
            self._parent_to_children[parent].remove(node)
        del self._child_to_parents[node]
        self._topo_sorted.remove(node)

    def parents_of(self, node: _T) -> FrozenSet[_T]:
        """Returns the immediate parents of the given node."""
        return frozenset(self._child_to_parents[node])

    def children_of(self, node: _T) -> FrozenSet[_T]:
        """Returns the immediate children of the given node."""
        return frozenset(self._parent_to_children[node])

    def _topo_sort(self) -> List[_T]:
        in_degrees = {
            node: len(parents) for node, parents in self._child_to_parents.items()
        }
        output: List[_T] = []
        # All the nodes that have no parents are our root nodes.
        q: Deque[_T] = collections.deque(
            node for (node, deg) in in_degrees.items() if deg == 0
        )
        while q:
            parent = q.popleft()
            del in_degrees[parent]
            for child in self._parent_to_children[parent]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    q.append(child)
            output.append(parent)
        if in_degrees:
            participating = tuple(in_degrees)
            raise CyclicGraphError(
                f"The graph contains a cycle involving {participating!r}"
            )
        return output

    def _add_edge_unsafe(self, *, child: _T, parent: _T) -> None:
        self._parent_to_children[parent].add(child)
        self._child_to_parents[child].add(parent)

    def _remove_edge(self, *, child: _T, parent: _T) -> None:
        self._parent_to_children[parent].discard(child)
        self._child_to_parents[child].discard(parent)


class CyclicGraphError(ValueError):
    """Error raised when you try to introduce a cycle into the graph."""
