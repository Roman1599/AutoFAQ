import pytest

from pages.base_page import BasePage
from pages.chat_page import ChatPage


class BaseTest:
    base_page: BasePage
    chat_page: ChatPage
    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.base_page = BasePage(driver)
        request.cls.chat_page = ChatPage(driver)


