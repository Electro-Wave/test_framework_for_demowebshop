import pytest
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from pages import MainPage
from utils import MyListener


def pytest_addoption(parser):
    parser.addoption('--url', action='store', default='http://demowebshop.tricentis.com/')
    parser.addoption('--browser', action='store', default='chrome', help='choose your browser')
    parser.addoption('--executor', action='store', default='127.0.0.1')
    parser.addoption('--local', action='store_true', default=False)
    parser.addoption('--enable_vnc', action='store_true', default=False)
    parser.addoption('--enable_video', action='store_true', default=False)
    parser.addoption('--browser_version', action='store', default='99.0')


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def browser(request):
    browser = request.config.getoption('--browser')
    local = request.config.getoption('--local')
    version = request.config.getoption('--browser_version')
    enable_vnc = request.config.getoption('--enable_vnc')
    enable_video = request.config.getoption('--enable_video')

    driver = None

    if local:
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            driver = EventFiringWebDriver(webdriver.Chrome(options=options), MyListener())
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            raise NotImplemented
        request.addfinalizer(driver.quit)
        driver.implicitly_wait(4)
        driver.maximize_window()

    else:
        executor_url = 'http://selenoid:4444/wd/hub'
        caps = {
            "browserName": browser,
            "browserVersion": version,
            "selenoid:options": {
                "enableVNC": enable_vnc,
                "enableVideo": enable_video
            }

        }

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.set_capability("enableVideo", enable_video)
            driver = EventFiringWebDriver(webdriver.Remote(command_executor=executor_url, options=options,
                                                           desired_capabilities=caps), MyListener())
            driver.implicitly_wait(3)
            driver.maximize_window()
            request.addfinalizer(driver.quit)
    return driver
