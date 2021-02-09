from model.contact import Contact
import re

def test_contact_info_vs_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test2", lastname="test3", homephone="12345678910",
                                   mobilephone="12345678911", workphone="12345678912", address="adresstest",
                                   secondaryphone="12345678913",
                                   email="email1@gmail.com", email2="email2@gmail.com", email3="email3@gmail.com"))
    for index in range(len(db.get_contact_list())):
        contact_fr_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)[index]
        contact_fr_db = db.get_contact_list()[index]
        assert contact_fr_home_page.firstname == contact_fr_db.firstname
        assert contact_fr_home_page.lastname == contact_fr_db.lastname
        assert contact_fr_home_page.address == contact_fr_db.address
        assert contact_fr_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_fr_db)
        assert contact_fr_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_fr_db)


def clear(s):
    return re.sub("[./() -]", "", s)

def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))


def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))