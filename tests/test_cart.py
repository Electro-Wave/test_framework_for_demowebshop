import allure
import pytest
from pages import MainPage
from pages import CartPage


@pytest.fixture
def add_item_to_cart(browser, url):
    page = MainPage(browser)
    page.open_page(url)
    page.click_books_link()
    page.add_product_to_cart()
    page.click_to_cat()


@allure.feature("Корзина")
@allure.title("Добавить товав в корзину")
@pytest.mark.cart
def test_add_product_cart(add_item_to_cart, browser):
    page = CartPage(browser)
    page.should_be_form_order_summary()
    page.amount_of_items_with_cart(1)


@allure.feature("Корзина")
@allure.title("Удаление товара из корзины")
@pytest.mark.cart
def test_delete_item_in_cart(add_item_to_cart, browser):
    page = CartPage(browser)
    page.should_be_form_order_summary()
    page.click_checkbox_remove()
    page.click_button_update_cart()
    page.should_be_empty_cart()
