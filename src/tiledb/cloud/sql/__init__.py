from typing import Optional

from tiledb.cloud.sql._execution import exec
from tiledb.cloud.sql._execution import exec_and_fetch
from tiledb.cloud.sql._execution import exec_async
from tiledb.cloud.sql.db_api_exceptions import *
from tiledb.cloud.sql.tiledb_connection import TileDBConnection

last_sql_task_id: Optional[str] = None

# Required by the Python DB API
apilevel = "2.0"
threadsafety = 2
paramstyle = "qmark"
connect = TileDBConnection

__all__ = (
    "exec",
    "exec_and_fetch",
    "exec_async",
    "last_sql_task_id",
    "TileDBConnection",
    "InterfaceError",
    "DatabaseError",
    "ProgrammingError",
    "DataError",
    "OperationalError",
    "IntegrityError",
    "InternalError",
    "NotSupportedError",
    "connect",
)
