import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    REMOVE_FROM_CART_CHECKBOX = (By.CSS_SELECTOR, '.remove-from-cart')
    PRODUCT_UNIT_PRICE = (By.CSS_SELECTOR, '.product-unit-price')
    QTY_FILED = (By.CSS_SELECTOR, '.qty-input')
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, '.update-cart-button')
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, '.continue-shopping-button')
    TOTAL = (By.CSS_SELECTOR, '.product-subtotal')
    TERMS_OF_SERVICE_CHECKBOX = (By.CSS_SELECTOR, '#termsofservice')
    SUB_TOTAL = (By.CSS_SELECTOR, '.nobr > span.product-price')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.order-total')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')
    FORM_ORDER_SUMMARY_CONTENT = (By.CSS_SELECTOR, 'form[action="/cart"')
    CART_ITEM_ROW = (By.CSS_SELECTOR, '.cart-item-row')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product-name')
    PRODUCT_ATTRIBUTES = (By.CSS_SELECTOR, '.attributes')
    LINK_EDIT = (By.CSS_SELECTOR, '.edit-item')
    EMPTY_ORDER_SUMMARY_CONTENT = (By.CSS_SELECTOR, '.order-summary-content')

    def amount_of_items_with_cart(self, amount):
        self._amount_of_elements_with_class_name(self.CART_ITEM_ROW, amount)

    def should_be_empty_cart(self):
        with allure.step("Проверяю наличие пустой корзины"):
            assert self._get_text(self.EMPTY_ORDER_SUMMARY_CONTENT) == 'Your Shopping Cart is empty!'
            self._is_not_present(self.FORM_ORDER_SUMMARY_CONTENT)

    def should_be_form_order_summary(self):
        with allure.step('Проверяю наличие формы заказа'):
            self._is_present(self.FORM_ORDER_SUMMARY_CONTENT)

    def click_link_edit_product(self):
        with allure.step('Нажимаю на кнопку Edit'):
            self._click(self.LINK_EDIT)

    def click_checkbox_remove(self):
        with allure.step('Нажимаю на чекбокс remove'):
            self._click(self.REMOVE_FROM_CART_CHECKBOX)

    def click_button_update_cart(self):
        with allure.step('Нажимаю на кнопку update'):
            self._click(self.UPDATE_CART_BUTTON)

    def click_button_continue_shopping(self):
        with allure.step('Нажимаю на кнопку continue shopping'):
            self._click(self.CONTINUE_SHOPPING_BUTTON)

    def click_button_checkout(self):
        with allure.step('Нажимаю на кнопку chekout'):
            self._click(self.CHECKOUT_BUTTON)

    def click_terms_of_service_checkbox(self):
        with allure.step('Нажимаю на чекбокс terms of service'):
            self._click(self.TERMS_OF_SERVICE_CHECKBOX)

    def click_product_name(self):
        with allure.step('Нажимаю на ссылку наименование товара'):
            self._click(self.PRODUCT_NAME)

    def input_field_qty(self, value):
        with allure.step(f'Ввожу в поле qty: {value}'):
            self._input(self.QTY_FILED, value)

    def check_change_price(self, expected_price: float):
        total_price = float(self._get_text(self.TOTAL))
        assert total_price == expected_price, f'expected price {expected_price} got {total_price}'
