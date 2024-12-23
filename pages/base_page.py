from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from tests_data.data import Links
from tests_data.locators import Locators

class BasePage:
    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(driver,10,poll_frequency=1)

    def open_page(self):
        links = Links()
        with allure.step(f"Open {links.MAIN_PAGE} page"):
            self.driver.get(links.MAIN_PAGE)



    def open_chat(self):
        with allure.step("открыть чат"):
            self.wait.until(EC.element_to_be_clickable(Locators.BUTTON_CHAT)).click()


    def is_open_chat(self):
        with allure.step("чат открыт"):
            self.wait.until(EC.visibility_of_element_located(Locators.CHAT_HEADER))
            self.make_screen("_чат открыт_")



    def close_chat(self):
        with allure.step("закрыть чат"):
            self.wait.until(EC.element_to_be_clickable(Locators.BUTTON_CLOSE_CHAT_UP)).click()

    def is_close_chat(self):
        with allure.step("чат закрыт"):
            self.wait.until(EC.visibility_of_element_located(Locators.BUTTON_CHAT))
            self.make_screen("_чат закрыт_")


    def make_screen(self, screen_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screen_name,
            attachment_type=AttachmentType.PNG
        )


