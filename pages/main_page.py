import allure
from selenium.webdriver.common.by import By
from pages import BasePage
from pages.common import Header


class MainPage(BasePage):
    ADD_T0_CART_BUTTON = (By.CSS_SELECTOR, '.product-box-add-to-cart-button')

    def add_product_to_cart(self):
        with allure.step('Наживаю на кнопку add to cart'):
            self._click(self.ADD_T0_CART_BUTTON)

    def click_books_link(self):
        with allure.step('Нажимаю на католог товаров Books'):
            self._click(Header.Catalog.BOOKS)

    def click_to_cat(self):
        with allure.step('Нажимаю на корзину товаров'):
            self._click(Header.SHOPPING_CART)
