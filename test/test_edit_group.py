from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="1", header="2", footer="3"))