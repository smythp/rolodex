from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class Contact(Table, tablename="contact"):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2022-03-23T21:38:23:483378"
VERSION = "0.71.1"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="yolodex", description=DESCRIPTION
    )

    manager.add_table("Relationship", tablename="relationship")

    manager.add_table("Interaction", tablename="interaction")

    manager.add_column(
        table_class_name="Relationship",
        tablename="relationship",
        column_name="first_contact",
        db_column_name="first_contact",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Contact,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    manager.add_column(
        table_class_name="Relationship",
        tablename="relationship",
        column_name="second_contact",
        db_column_name="second_contact",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Contact,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
    )

    return manager
