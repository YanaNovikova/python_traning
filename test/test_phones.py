import re
from random import randrange
from model.contact import Contact

'''
def test_phones_on_homepage(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
'''

def test_phones_on_homepage_all(app, db):
    old_contacts = db.get_contact_list()
    contact_from_homepage = app.contact.get_contact_list()
    list1 = sorted(old_contacts, key=Contact.id_max)
    list2 = sorted(contact_from_homepage, key=Contact.id_max)
    assert len(list1) == len(list2)
    for i in range(0, len(old_contacts)):
        assert old_contacts.lastname[i] == contact_from_homepage.lastname[i]

'''
def test_phones_on_viewpage(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_viewpage = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_viewpage.home == contact_from_edit_page.home
    assert contact_from_viewpage.mobile == contact_from_edit_page.mobile
    assert contact_from_viewpage.work == contact_from_edit_page.work
    assert contact_from_viewpage.phone2 == contact_from_edit_page.phone2
'''

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))


