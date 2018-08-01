import re
from random import randrange
from fixture.orm import ORMFixture
from model.contact import Contact

dat = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_LFA_on_viewpage(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_homepage.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_homepage.address == clear(contact_from_edit_page.address)


def test_LFA_on_viewpage_all(app):
    db_contacts = dat.get_contact_list()
    contact_from_homepage = app.contact.get_contact_list()
    list1 = sorted(db_contacts, key=Contact.id_max)
    list2 = sorted(contact_from_homepage, key=Contact.id_max)
    assert len(list1) == len(list2)
    for i in range(0, len(db_contacts)):
        assert list1[i].lastname == list2[i].lastname
        assert list1[i].firstname == list2[i].firstname
        assert list1[i].address == list2[i].address


def clear(s):
    return re.sub("[() /-]", "", s)