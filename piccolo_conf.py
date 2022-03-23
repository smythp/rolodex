from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry


DB = PostgresEngine(
    config={
        "database": "yolodex",
        "user": "yolodex",
        "password": "makecontacts",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["yolodex.piccolo_app", "piccolo_admin.piccolo_app"]
)
