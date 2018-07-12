import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.home == clear(contact_from_edit_page.home)
    assert contact_from_homepage.mobile == clear(contact_from_edit_page.mobile)
    assert contact_from_homepage.work == clear(contact_from_edit_page.work)
    assert contact_from_homepage.phone2 == clear(contact_from_edit_page.phone2)

def clear(s):
    return re.sub("[() -]", "", s)

