from selenium.webdriver.common.by import By


class Header:
    SHOPPING_CART = (By.CSS_SELECTOR, ".ico-cart")

    class Catalog:
        BOOKS = (By.CSS_SELECTOR, 'a[href="/books"]')
