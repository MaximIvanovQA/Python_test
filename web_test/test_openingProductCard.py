# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 31.08.2022 22:35
# @My Git  : https://github.com/MaximIvanovQA/Python_test

from web_client.application import Application
import pytest
from web_client.model.user import Standard


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.closeBrowsers)
    return fixture


def test_opening_product_card(app):
    app.session.login(Standard("standard_user", "secret_sauce"))
    app.inventory.open_product_card("item_4_title_link")
    app.session.logout()
