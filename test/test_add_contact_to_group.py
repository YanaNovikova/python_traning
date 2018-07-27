from model.contact import Contact
from random import randrange


def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create1(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1",home="1", mobile="1", work="1", fax="1", email="1", email2="1", email3="1", homepage="1",byear="2000", address2="1", phone2="1", notes="1"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.add_contact_to_group(index)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)