from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, UUID, Timestamptz, Date, Integer, ForeignKey
import enum


class RelationshipType(str, enum.Enum):
    colleague = "colleague"
    friend = "friend"
    relative = "relative"
    partner = "partner"
    ex = "ex"
    child = "child"
    teacher = "teacher"
    student = "student"





class Contact(Table):

    firstname = Varchar()
    # last_modified = Timestamptz()
    # created = Timestamptz()
    lastname = Varchar()
    middleName = Varchar()
    suffix = Varchar()
    nickname = Varchar()
    birthday = Date()
    gender = Varchar()
    address_1 = Varchar()
    address_2 = Varchar()
    city = Varchar()
    secondary = Boolean()
    zip = Varchar()
    title = Varchar()
    email = Varchar()
    phone = Integer()
    notes = Varchar()


class Relationship(Table):
    first_contact = ForeignKey(references=Contact)
    second_contact = ForeignKey(references=Contact,)

    type= Varchar(choices=RelationshipType)



class Interaction(Table):
    datetime_interaction = Timestamptz
    occured = Boolean
    suggested_interaction = Boolean
    link = Varchar
    interaction_text = Varchar
    notes_prior = Varchar
    notes = Varchar       
    last_modified = Timestamptz
    created = Timestamptz

    class ModeInteraction(enum.Enum):
        zoom = "zoom"
        lunch = "lunch"
        dinner = "dinner"
        coffee = "coffee"
        drinks = "drinks"
        phone = "phone"
        meeting = "meeting"
        event = "event"
        random = "random"

    mode = Varchar(choices=ModeInteraction)
