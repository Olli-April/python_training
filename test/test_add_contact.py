# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.create(Contact(first_name="Lili", last="And", address="New York"))
        app.session.logout()