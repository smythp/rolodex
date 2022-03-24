from pydantic import BaseModel
import enum

import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from utilities import now_utc


from yolodex.endpoints import HomeEndpoint
from yolodex.piccolo_app import APP_CONFIG


from yolodex.tables import Contact, Relationship


from models import RelationshipIn, RelationshipOut, ContactIn, ContactOut



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


#####

@app.get("/relationships/", response_model=t.List[RelationshipOut])
async def relationships():
    return await Relationship.select().order_by(Relationship.id)


@app.post("/relationships/", response_model=RelationshipOut)
async def create_relationship(relationship_model: RelationshipIn):
    # relationship_model_dict = relationship_model.dict()
    # relationship_model_dict['last_modified'] = now_utc()

    relationship = Relationship(**relationship_model.dict())

    await relationship.save()
    return relationship.to_dict()





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
