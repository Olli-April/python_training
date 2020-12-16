# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_new_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(first_name="Lili", last="And", address="New York"))
        app.session.logout()