from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="Group_Edit", header="Edit_header", footer="Edit_footer"))