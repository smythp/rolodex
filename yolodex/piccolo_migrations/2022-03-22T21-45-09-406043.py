from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2022-03-22T21:45:09:406043"
VERSION = "0.71.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="yolodex", description=DESCRIPTION
    )

    manager.add_table("Contact", tablename="contact")

    manager.drop_table(class_name="DrifttUser", tablename="driftt_user")

    return manager
