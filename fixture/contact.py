from model.contact import Contact
import re
from fixture.orm import ORMFixture

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value_contact(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value_contact("firstname", contact.firstname)
        self.change_field_value_contact("middlename", contact.middlename)
        self.change_field_value_contact("lastname", contact.lastname)
        self.change_field_value_contact("nickname", contact.nickname)
        self.change_field_value_contact("title", contact.title)
        self.change_field_value_contact("company", contact.company)
        self.change_field_value_contact("address", contact.address)
        self.change_field_value_contact("home", contact.home)
        self.change_field_value_contact("mobile", contact.mobile)
        self.change_field_value_contact("work", contact.work)
        self.change_field_value_contact("fax", contact.fax)
        self.change_field_value_contact("email", contact.email)
        self.change_field_value_contact("email2", contact.email2)
        self.change_field_value_contact("email3", contact.email3)
        self.change_field_value_contact("homepage", contact.homepage)
        self.change_field_value_contact("byear", contact.byear)
        self.change_field_value_contact("address2", contact.address2)
        self.change_field_value_contact("phone2", contact.phone2)
        self.change_field_value_contact("notes", contact.notes)

    def create1(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # fill contact form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[6]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()
        self.contact_cache = None

    def create2(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home()
        self.select_contact_by_index(index)
        # submit delete
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[@class='left']/input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.return_home()
        self.select_contact_by_id(id)
        # submit delete
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[@class='left']/input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def edit_first_contact(self, index, contact):
        wd = self.app.wd
        self.return_home()
        self.select_first_contact()
        self.open_modification_form(index)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.return_homepage()
        self.contact_cache = None

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def return_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Add")) > 0):
            wd.find_element_by_link_text("home").click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_home()
        self.open_modification_form(index)
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.return_homepage()
        self.contact_cache = None

    def open_modification_form(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_home()
            self.contact_cache = []
            for table in wd.find_elements_by_name('entry'):
                element = table.find_elements_by_css_selector('td')
                text1 = element[1].text
                text2 = element[2].text
                id = element[0].find_element_by_name("selected[]").get_attribute("id")
                all_phones = element[5].text
                all_emails = element[4].text
                address = element[3].text
                self.contact_cache.append(Contact(lastname=text1, firstname=text2, id=id,
                                                  all_phones_from_homepage=all_phones, all_emails_from_homepage=all_emails,
                                                  address=address))
        return list(self.contact_cache)

    def open_edit_by_index(self, index):
        wd = self.app.wd
        self.return_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_view_by_index(self, index):
        wd = self.app.wd
        self.return_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email").get_attribute("value")
        email3 = wd.find_element_by_name("email").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=homephone, work=workphone,
                       mobile=mobilephone, phone2=phone2, email=email, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone, phone2=phone2)

    def add_contact_to_group(self, index, id):
        wd = self.app.wd
        self.return_home()
        contact = wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % id).click()
        if contact != ORMFixture.get_contacts_in_group:
            wd.find_element_by_name("add").click()
        else:
            wd.find_elements_by_name("selected[]")[index].click()
            wd.find_element_by_name("to_group").click()
            wd.find_element_by_css_selector("option[value='%s']" % id).click()
        self.return_home()
        self.contact_cache = None

    def delete_contact_to_group(self, index, id):
        wd = self.app.wd
        self.return_home()
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % id).click()
        if ORMFixture.get_contacts_in_group is None:
            wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % id).click()
            wd.find_elements_by_name("selected[]")[index].click()
            wd.find_element_by_name("remove").click()
        else:
            wd.find_elements_by_name("selected[]")[index].click()
            wd.find_element_by_name("remove").click()
        self.return_home()
        wd.find_element_by_xpath("//select[@name='group']/option[@value='']").click()
        self.contact_cache = None


