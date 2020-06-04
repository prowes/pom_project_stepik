from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.TAG_NAME, "h1")
    ALERT = (By.CSS_SELECTOR, ".alertinner strong")