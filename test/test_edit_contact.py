
from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="New Name", last="New Lastname", address="New Address"))
    app.session.logout()
