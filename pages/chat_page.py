
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.keys import Keys
import time
from pages.base_page import BasePage
from tests_data.locators import Locators

class ChatPage(BasePage):

    def send_message(self, text):
        with allure.step("Отправка сообщения в чат"):
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).clear()
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).send_keys(text)
            self.wait.until(EC.element_to_be_clickable(Locators.SEND_BUTTON)).click()
            self.make_screen("_сообщение отправлено_")

    def send_message_enter(self, text):
        with allure.step("Отправка сообщения в чат кнопкой enter"):
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).clear()
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).send_keys(text)
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).send_keys(Keys.ENTER)
            self.make_screen("_сообщение отправлено нопкой Enter_")

    def get_first_message_text(self):
        with allure.step("Получение текста первого сообщения"):
            first_message = self.wait.until(EC.presence_of_element_located(Locators.FIRST_MESSAGE))
            return first_message.text

    def verify_message_sent(self, text):
        with allure.step("Проверка отправленного сообщения"):
            actual_text = self.get_first_message_text()
            assert actual_text == text, f"Ожидали: '{text}', получили: '{actual_text}'"



    def send_emoji(self):
        with allure.step("Отправка эможи"):
            self.wait.until(EC.element_to_be_clickable(Locators.TEXT_FIELD)).clear()
            self.wait.until(EC.element_to_be_clickable(Locators.EMOJI_BUTTON)).click()
            self.wait.until(EC.element_to_be_clickable(Locators.EMODJI_FIRST)).click()
            self.wait.until(EC.element_to_be_clickable(Locators.EMOJI_BUTTON)).click()
            self.wait.until(EC.element_to_be_clickable(Locators.EMODJI_SECOND)).click()
            self.wait.until(EC.element_to_be_clickable(Locators.SEND_BUTTONN)).click()
            self.make_screen("эможи отправлено_")

    def check_form(self):
        with allure.step("проверка отображения формы"):
            self.wait.until(EC.visibility_of_element_located(Locators.FORM_PANEL_LABEL))
            self.wait.until(EC.visibility_of_element_located(Locators.FORM_PANEL_LABEL_EMAIL))
            self.wait.until(EC.visibility_of_element_located(Locators.FORM_SEND_BUTTON))
            self.make_screen("_форма отобразилась_")

    def check_no_form(self):
        with allure.step("проверка что формы нет"):
            self.wait.until(EC.invisibility_of_element(Locators.FORM_PANEL_LABEL))
            self.wait.until(EC.invisibility_of_element(Locators.FORM_PANEL_LABEL_EMAIL))
            self.wait.until(EC.invisibility_of_element(Locators.FORM_SEND_BUTTON))
            self.make_screen("_формы нет_")

    def add_form(self,name,email):
        with allure.step("проверка отправки формы"):
            self.wait.until(EC.element_to_be_clickable(Locators.FORM_NAME)).send_keys(name)
            self.wait.until(EC.element_to_be_clickable(Locators.FORM_EMAIL)).send_keys(email)
            self.make_screen("форма заполнена_")
            self.wait.until(EC.element_to_be_clickable(Locators.FORM_SEND_BUTTON)).click()
