from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form_contact(contact)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_form_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.last)
        self.change_field_value("address", contact.address)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_form_contact(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(last=lastname, first_name=firstname, id=id))
            return list(self.contact_cache)
