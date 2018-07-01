# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create1(Contact(firstname="1", middlename="1", lastname="1", nickname="1", title="1", company="1", address="1", home="1", mobile="1", work="1", fax="1", email="1", email2="1", email3="1", homepage="1", byear="2000", address2="1", phone2="1", notes="1"))
    app.contact.modify_first_contact(Contact(firstname="New"))

