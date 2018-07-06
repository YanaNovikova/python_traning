# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test",
                                address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test",
                                email3="test", homepage="test", byear="1995", address2="test", phone2="test", notes="test")
    app.contact.create1(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)


#def test_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    app.contact.create2(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", address2="", phone2="", notes=""))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
