from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New Name"))
    app.session.logout()

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="New Address"))
    app.session.logout()
