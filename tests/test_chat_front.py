

import allure
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.base import BaseTest


@allure.feature("проверки чатов")
class TestChats(BaseTest):

    @allure.title("Проверка откытия чата")
    @allure.severity("Critical")
    def test_open_chat(self):
        self.base_page.open_page()
        self.base_page.open_chat()
        self.base_page.is_open_chat()
        self.base_page.close_chat()
        self.base_page.is_close_chat()

    @allure.title("Проверка отправки сообщения в чат")
    @allure.severity("Critical")
    def test_send_message(self):
        self.base_page.open_page()
        self.base_page.open_chat()
        self.base_page.is_open_chat()
        self.chat_page.send_message("тестовое сообщение")
        self.chat_page.get_first_message_text()
        self.chat_page.verify_message_sent("тестовое сообщение")
        self.base_page.close_chat()
        self.base_page.is_close_chat()

    @allure.title("Проверка отправки сообщения в чат кнопкой enter")
    @allure.severity("Critical")
    def test_send_message_enter(self):
        self.base_page.open_page()
        self.base_page.open_chat()
        self.base_page.is_open_chat()
        self.chat_page.send_message_enter("тестовое сообщение2")
        self.chat_page.get_first_message_text()
        self.chat_page.verify_message_sent("тестовое сообщение")
        self.base_page.close_chat()
        self.base_page.is_close_chat()



    @allure.title("Проверка отправки эможи")
    @allure.severity("Critical")
    def test_send_message_emoji(self):
        self.base_page.open_page()
        self.base_page.open_chat()
        self.base_page.is_open_chat()
        self.chat_page.send_emoji()
        self.base_page.close_chat()
        self.base_page.is_close_chat()

    @allure.title("Проверка отправки формы")
    @allure.severity("Critical")
    def test_send_form(self):
        self.base_page.open_page()
        self.base_page.open_chat()
        self.base_page.is_open_chat()
        self.chat_page.check_form()
        self.chat_page.add_form("Иван","ivanov@mail.ru")
        self.chat_page.check_no_form()
        self.base_page.close_chat()
        self.base_page.is_close_chat()

