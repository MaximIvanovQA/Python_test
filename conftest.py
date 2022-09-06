# -*- coding: utf-8 -*-
# @Author  : Maksim Ivanov
# @Time    : 31.08.2022 23:13
# @My Git  : https://github.com/MaximIvanovQA/Python_test
from web_client.application import Application
import pytest

@pytest.fixture(scope= "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.closeBrowsers)
    return fixture