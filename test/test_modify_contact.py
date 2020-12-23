from model.contact import Contact

def test_modify_contact_name(app):
    if app.contact.count() < 2:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(first_name="New Name"))

def test_modify_contact_address(app):
    if app.contact.count() < 2:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify_first_contact(Contact(address="New Address"))

