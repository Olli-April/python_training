# -*- coding: utf-8 -*-
import pytest
from new.contact import Contact
from new.appcontact import ApplicationSecond

@pytest.fixture
def app(request):
    fixture = ApplicationSecond()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(first_name="Lili", last="And", address="New York"))
        app.logout()