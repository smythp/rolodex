from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, UUID, Timestamptz, Date, Integer


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
