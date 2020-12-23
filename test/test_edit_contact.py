
from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() < 2:
        app.contact.create(Contact(first_name="test"))
    app.contact.edit_first_contact(Contact(first_name="New Name", last="New Lastname", address="New Address"))

