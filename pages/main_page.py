from selenium.webdriver.common.by import By
from pages import BasePage
from pages.common import Header


class MainPage(BasePage):
    ADD_T0_CART_BUTTON = (By.CSS_SELECTOR, '.product-box-add-to-cart-button')

    def add_product_to_cart(self):
        el = self._click(self.ADD_T0_CART_BUTTON)

    def click_books_link(self):
        el = self._click(Header.Catalog.BOOKS)
        return self

    def click_to_cat(self):
        return self._click(Header.SHOPPING_CART)