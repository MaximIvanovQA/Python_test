# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 20.08.2022 11:06
# @My Git  : https://github.com/MaximIvanovQA/Python_test

from web_client.application import Application
import pytest
from web_client.model.user import Standard


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.closeBrowsers)
    return fixture


def test_login(app):
    app.session.login(Standard("standard_user", "secret_sauce"))
    app.session.logout()



