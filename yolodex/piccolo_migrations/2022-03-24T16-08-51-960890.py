from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from enum import Enum
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2022-03-24T16:08:51:960890"
VERSION = "0.71.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="yolodex", description=DESCRIPTION
    )

    manager.add_column(
        table_class_name="Interaction",
        tablename="interaction",
        column_name="mode",
        db_column_name="mode",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": Enum(
                "ModeInteraction",
                {
                    "zoom": "zoom",
                    "lunch": "lunch",
                    "dinner": "dinner",
                    "coffee": "coffee",
                    "drinks": "drinks",
                    "phone": "phone",
                    "meeting": "meeting",
                    "event": "event",
                    "random": "random",
                },
            ),
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Relationship",
        tablename="relationship",
        column_name="type",
        db_column_name="type",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": Enum(
                "RelationshipType",
                {
                    "colleague": "colleague",
                    "friend": "friend",
                    "relative": "relative",
                    "partner": "partner",
                    "ex": "ex",
                    "child": "child",
                    "teacher": "teacher",
                    "student": "student",
                },
            ),
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
