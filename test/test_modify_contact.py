from model.contact import Contact

def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(first_name="New Name"))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="New Address"))

