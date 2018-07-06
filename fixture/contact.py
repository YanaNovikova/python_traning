from model.contact import Contact


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

    def create2(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_homepage()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_home()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # submit edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[1]").click()
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.return_homepage()

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def return_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Add")) > 0):
            wd.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        #open modification form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        #submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[1]").click()
        self.return_homepage()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            wd.find_elements_by_css_selector('td')
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(lastname=text, firstname=text, id=id))
        return contacts

