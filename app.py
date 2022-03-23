import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from utilities import now_utc


from yolodex.endpoints import HomeEndpoint
from yolodex.piccolo_app import APP_CONFIG
from yolodex.tables import Contact


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


ContactIn: t.Any = create_pydantic_model(table=Contact, model_name="ContactIn")
ContactOut: t.Any = create_pydantic_model(
    table=Contact, include_default_columns=True, model_name="ContactOut"
)


@app.get("/contacts/", response_model=t.List[ContactOut])
async def contacts():
    return await Contact.select().order_by(Contact.id)


@app.post("/contacts/", response_model=ContactOut)
async def create_contact(contact_model: ContactIn):
    
    contact_model_dict = contact_model.dict()

    # contact_model_dict['last_modified'] = now_utc()

    contact = Contact(**contact_model.dict())

    await contact.save()
    return contact.to_dict()


@app.put("/contacts/{contact_id}/", response_model=ContactOut)
async def update_contact(contact_id: int, contact_model: ContactIn):
    contact = await Contact.objects().get(Contact.id == contact_id)
    if not contact:
        return JSONResponse({}, status_code=404)

    for key, value in contact_model.dict().items():
        setattr(contact, key, value)

    await contact.save()

    return contact.to_dict()


@app.delete("/contacts/{contact_id}/")
async def delete_contact(contact_id: int):
    contact = await Contact.objects().get(Contact.id == contact_id)
    if not contact:
        return JSONResponse({}, status_code=404)

    await contact.remove()

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
