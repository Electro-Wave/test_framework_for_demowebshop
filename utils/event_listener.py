import allure
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        with allure.step(f'нашел элемент {value}'):
            pass

    def after_click(self, element, driver):
        with allure.step(f'кликаю по элементу {element}'):
            pass

    def on_exception(self, exception, driver):
        print(f'выбрасываю исключение {exception}')
        allure.attach(driver.get_screenshot_as_png(),
                      driver.session_id,
                      allure.attachment_type.PNG
                      )

    def before_navigate_to(self, url, driver):
        with allure.step(f'открываю {url}'):
            pass

    def before_quit(self, driver):
        with allure.step(f'закрываю браузер {driver}'):
            pass
