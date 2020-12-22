# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
        app.contact.create(Contact(first_name="Lili", last="And", address="New York"))