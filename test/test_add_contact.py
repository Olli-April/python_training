# -*- coding: utf-8 -*-
from model.contact import Contact
from data.contacts import constant as testdata
import pytest


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







#address=random_string("address", 15), middlename=random_string("middlename", 20),
# address2=random_string("address2", 10), email=random_string("email", 10),
# email2=random_string("email2", 10), email3=random_string("email3", 10), homephone=random_string("homephone", 10),
# workphone = random_string("workphone", 10), secondaryphone = random_string("secondaryphone", 10)