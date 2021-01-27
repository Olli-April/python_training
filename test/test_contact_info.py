from model.contact import Contact
from random import randrange
import re

def test_contact_info_vs_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test2", lastname="test3", homephone="12345678910",
                                   mobilephone="12345678911", workphone="12345678912", address="adresstest",
                                   secondaryphone="12345678913",
                                   email="email1@gmail.com", email2="email2@gmail.com", email3="email3@gmail.com"))
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

def test_contact_info_home_vs_edit(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test2", lastname="test3", homephone="12345678910",
                                   mobilephone="12345678911", workphone="12345678912", address="adresstest",
                                   secondaryphone="12345678913",
                                   email="email1@gmail.com", email2="email2@gmail.com", email3="email3@gmail.com"))
        list_contacts = app.contact.get_contact_list()
        index = randrange(len(list_contacts))
        contact_from_home_page = app.contact.get_contact_list()[index]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname
        assert contact_from_home_page.address == contact_from_edit_page.address
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_from_edit_page)

def test_contact_info_home_vs_view(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test2", lastname="test3", homephone="12345678910",
                                   mobilephone="12345678911", workphone="12345678912", address="adresstest",
                                   secondaryphone="12345678913",
                                   email="email1@gmail.com", email2="email2@gmail.com", email3="email3@gmail.com"))
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[./() -]", "", s)

def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))