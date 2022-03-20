from piccolo.table import Table
from piccolo.columns import Varchar, Boolean, UUID, Date


class DrifttUser(Table):
    # id = UUID()
    first_name = Varchar()
    last_name = Varchar()
    email = Varchar()
    last_modified = Date()
