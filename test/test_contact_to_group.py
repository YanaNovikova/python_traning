from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture
import random

dat = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create1(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1",home="1", mobile="1", work="1", fax="1", email="1", email2="1", email3="1", homepage="1",byear="2000", address2="1", phone2="1", notes="1"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="testtest"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    group = random.choice(groups)
    index = randrange(len(contacts))
    contact_to_group = dat.get_contacts_in_group(group)
    if len(contact_to_group) == len(contacts):
        app.contact.create1(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1",home="1", mobile="1", work="1", fax="1", email="1", email2="1", email3="1", homepage="1",byear="2000", address2="1", phone2="1", notes="1"))
    app.contact.add_contact_to_group(index, group.id)
    new_contacts = db.get_contact_list()
    assert len(contacts) == len(new_contacts)
    assert sorted(contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)


def test_delete_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create1(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1",home="1", mobile="1", work="1", fax="1", email="1", email2="1", email3="1", homepage="1",byear="2000", address2="1", phone2="1", notes="1"))
    elif len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="testtest"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    group = random.choice(groups)
    index = randrange(len(contacts))
    contact_to_group = dat.get_contacts_in_group(group)
    if len(contact_to_group) == 0:
        app.contact.add_contact_to_group(index, group.id)
    app.contact.delete_contact_to_group(index, group.id)
    new_contacts = db.get_contact_list()
    assert len(contacts) == len(new_contacts)
    assert sorted(contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)