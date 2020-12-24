
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
        self.fill_form_contact(contact)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

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
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_form_contact(new_contact_data)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        self.fill_form_contact(contact)
        # submit edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_xpath("//input[@type='checkbox']").click()
        # submit delection
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def return_to_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("index.php"):
            wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_xpath("//input[@type='checkbox']"))
