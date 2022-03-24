import typing as t
from pydantic import BaseModel
import enum
from piccolo_api.crud.serializers import create_pydantic_model
from yolodex.tables import Contact, Relationship


from yolodex.tables import RelationshipType






ContactIn: t.Any = create_pydantic_model(table=Contact, model_name="ContactIn")
ContactOut: t.Any = create_pydantic_model(
    table=Contact, include_default_columns=True, model_name="ContactOut")

RelationshipPreprocessed: t.Any = create_pydantic_model(table=Relationship, model_name="RelationshipIn")        
RelationshipOut: t.Any = create_pydantic_model(
    table=Relationship, include_default_columns=True, model_name="RelationshipOut")


class RelationshipIn(RelationshipPreprocessed):

    type: RelationshipType
    
