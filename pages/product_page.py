from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()

    def should_be_book_title_on_page(self, title):
        self.title = title
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert title in book_title

    def should_be_book_price_on_page(self, price):
        self.price = price
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text[:-2]
        assert price in book_price

    def should_be_book_title_on_page_title(self, page_title):
        self.page_title = page_title
        assert self.browser.title in page_title

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
