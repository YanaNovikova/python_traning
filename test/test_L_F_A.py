import re
from random import randrange


def test_phones_on_viewpage(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_homepage.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_homepage.address == clear(contact_from_edit_page.address)

def clear(s):
    return re.sub("[() -]", "", s)