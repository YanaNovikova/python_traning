# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create1(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test", company="test", address="test", home="test", mobile="test", work="test", fax="test", email="test", email2="test", email3="test", homepage="test", byear="1995", address2="test", phone2="test", notes="test"))


def test_add_empty_contact(app):
    app.contact.create2(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", address2="", phone2="", notes=""))

