# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def randomstring(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                                home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="",
                                address2="", phone2="", notes="")] + [
    Contact(firstname=randomstring("firstname", 10), middlename=randomstring("middlename", 10), lastname=randomstring("lastname", 10),
            nickname=randomstring("nickname", 10), title=randomstring("title", 5), company=randomstring("company", 20), address=randomstring("address", 20),
            home=randomstring("home", 11), mobile=randomstring("mobile", 11), work=randomstring("work", 11), fax=randomstring("fax", 15),
            email=randomstring("email", 10), email2=randomstring("email2", 10), email3=randomstring("email3", 10), homepage=randomstring("homepage", 15),
            address2=randomstring("address2", 20), phone2=randomstring("phone2", 11), notes=randomstring("notes", 20))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])


def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create1(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_max) == sorted(new_contacts, key=Contact.id_max)
