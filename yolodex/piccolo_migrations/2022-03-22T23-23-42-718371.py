from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Timestamptz
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.defaults.timestamptz import TimestamptzNow


ID = "2022-03-22T23:23:42:718371"
VERSION = "0.71.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="yolodex", description=DESCRIPTION
    )

    manager.alter_column(
        table_class_name="Contact",
        tablename="contact",
        column_name="created",
        params={"default": TimestamptzNow()},
        old_params={"default": TimestampNow()},
        column_class=Timestamptz,
        old_column_class=Timestamp,
    )

    manager.alter_column(
        table_class_name="Contact",
        tablename="contact",
        column_name="last_modified",
        params={"default": TimestamptzNow()},
        old_params={"default": TimestampNow()},
        column_class=Timestamptz,
        old_column_class=Timestamp,
    )

    return manager
