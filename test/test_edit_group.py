from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group((Group(name="Group_Edit", header="Edit_header", footer="Edit_footer")))
    app.session.logout()