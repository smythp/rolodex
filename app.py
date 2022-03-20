import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from driftt.endpoints import HomeEndpoint
from driftt.piccolo_app import APP_CONFIG
from driftt.tables import DrifttUser


app = FastAPI(
    routes=[
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes,
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)


DrifttUserIn: t.Any = create_pydantic_model(table=DrifttUser, model_name="DrifttUserIn")
DrifttUserOut: t.Any = create_pydantic_model(
    table=DrifttUser, include_default_columns=True, model_name="DrifttUserOut"
)


@app.get("/users/", response_model=t.List[DrifttUserOut])
async def users():
    return await DrifttUser.select().order_by(DrifttUser.id)


@app.post("/users/", response_model=DrifttUserOut)
async def create_user(user_model: DrifttUserIn):
    user = DrifttUser(**user_model.dict())
    await user.save()
    return user.to_dict()


@app.put("/users/{user_id}/", response_model=DrifttUserOut)
async def update_user(user_id: int, user_model: DrifttUserIn):
    user = await User.objects().get(DrifttUser.id == user_id)
    if not user:
        return JSONResponse({}, status_code=404)

    for key, value in user_modell.dict().items():
        setattr(user, key, value)

    await user.save()

    return user.to_dict()


@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    user = await DrifttUser.objects().get(DrifttUser.id == user_id)
    if not user:
        return JSONResponse({}, status_code=404)

    await user.remove()

    return JSONResponse({})


@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
