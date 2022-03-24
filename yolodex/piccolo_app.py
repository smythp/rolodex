"""
Import all of the Tables subclasses in your app here, and register them with
the APP_CONFIG.
"""

# from .tables import (
#     Contact
# )

import os

from piccolo.conf.apps import AppConfig, table_finder


CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="yolodex",
    migrations_folder_path=os.path.join(
        CURRENT_DIRECTORY, "piccolo_migrations"
    ),
    # table_classes=[Contact],
    table_classes=table_finder(modules=["yolodex.tables"], exclude_imported=True),
    migration_dependencies=[],
    commands=[],
)
