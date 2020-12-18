
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form_contact(contact, wd)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    def fill_form_contact(self, contact, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//input[@type='checkbox']").click()
        # submit delection
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_form_contact(contact, wd)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()



    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
