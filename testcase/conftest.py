from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Config.config import TestData


@pytest.fixture(scope='class', autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.find_element(By.XPATH, "//input[@id='Email']").clear()
    driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(TestData.USERNAME)
    driver.find_element(By.XPATH, "//input[@id='Password']").clear()
    driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(TestData.PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption("--url")
