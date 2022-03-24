from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException


class BasePage:
    def __init__(self, driver=None, timeout=5):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, timeout)

    def open_page(self, url: str, path: str = ''):
        self._driver.get(url + path)

    def current_url_should_be(self, expected_url):
        if self._wait.until(EC.url_to_be(expected_url)):
            return True
        else:
            raise AssertionError(f'expected url:{expected_url}, got {self._driver.current_url}')

    def set_cookie(self, cookie):
        self._driver.add_cookie(cookie)

    def _is_present(self, locator):
        try:
            el = self._wait.until(EC.visibility_of_element_located(locator))
            return el
        except TimeoutException:
            raise AssertionError(f'element {locator} not found')

    def _is_not_present(self, locator):
        try:
            if self._driver.find_element(*locator).is_displayed():
                raise AssertionError(f"element {locator} found on page visible but it shouldn't be")
        except NoSuchElementException:
            return True

    def _click(self, locator):
        try:
            self._wait.until(EC.element_to_be_clickable(locator)).click()
        except TimeoutException:
            raise AssertionError(f'unable to click on element {locator}')

    def _input(self, locator, value):
        el = self._is_present(locator)
        el.clear()
        el.send_keys(value)

    def _get_text(self, locator):
        return self._is_present(locator).text

    def _amount_of_elements_with_class_name(self, locator, amount: int):
        elements = self._driver.find_elements(*locator)

        if len(elements) == amount:
            return elements
        else:
            raise AssertionError(f"expected amount {amount} got {len(elements)}")

    def _find_elements(self, locator):
        try:
            elements = self._driver.find_elements(*locator)
            return elements
        except WebDriverException as e:
            raise AssertionError(e)