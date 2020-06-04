from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import math

class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        sleep(5)
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def get_a_shown_book_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def verify_the_item_name_in_notification(self):
        notification_area = self.browser.find_element(*ProductPageLocators.ALERT)  # go deeper
        text_after_adding = notification_area.text
        assert text_after_adding == self.get_a_shown_book_name()

    def no_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.ALERT), \
            "Success message is presented"

    def success_message_disappears(self, timeout=4):
        assert self.is_disappeared(*ProductPageLocators.ALERT), \
            "Success message does not disappear"