from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2022-03-23T21:35:42:701862"
VERSION = "0.71.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="yolodex", description=DESCRIPTION
    )

    manager.drop_column(
        table_class_name="Contact",
        tablename="contact",
        column_name="created",
        db_column_name="created",
    )

    manager.drop_column(
        table_class_name="Contact",
        tablename="contact",
        column_name="last_modified",
        db_column_name="last_modified",
    )

    return manager
