![Build Status](http://51.250.103.162:8080/buildStatus/icon?job=test_demoshop)



## Тестовый фреймворк автоматизации тестирования для освоение Jenkins [демо интерент магазина](http://demowebshop.tricentis.com/) с генерацией отчетов в Allure

На текущий момент времени реализованы только минимальные тесты проверки корзины 

```python
#test_cart.py
@allure.feature('Корзина')
@allure.title('Добавить товав в корзину')
@pytest.mark.cart
def test_add_product_cart(add_item_to_cart, browser):
    page = CartPage(browser)
    page.should_be_form_order_summary()
    page.amount_of_items_with_cart(1)


@allure.feature('Корзина')
@allure.title('Удаление товара из корзины')
@pytest.mark.cart
def test_delete_item_in_cart(add_item_to_cart, browser):
    page = CartPage(browser)
    page.should_be_form_order_summary()
    page.click_checkbox_remove()
    page.click_button_update_cart()
    page.should_be_empty_cart()

            ....
```
Для запуска тестов в selenoid (по умолчанию используется image docker - selenoid/chrome:99.0):
```shell
pytest 
```

Для запуска локального браузера (только chrome, firefox):
``` shell
pytest --local --browser=chrome --browser_version=99.0
```
