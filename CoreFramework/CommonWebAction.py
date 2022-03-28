import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from webdriver_manager import driver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonWebAction:
    def __init__(self, driver):
        self.driver = driver

    def enterValueInTextBox(self, locator_type, locator, value):
        try:
            self.driver.find_element(locator_type, locator).send_keys(value)
        except Exception as e:
            print(e.message)

    def clearValueFromTextBox(self, locator_type, locator):
        try:
            self.driver.find_element(locator_type, locator).clear()
        except Exception as e:
            print(e.message)

    def clickOnElement(self, locator_type, locator):
        try:
            self.driver.find_element(locator_type, locator).click()
        except Exception as e:
            print(e.message)

    def switchToFrame(self, frame_id):
        try:
            self.driver.switch_to.frame(frame_id)
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e.message)

    def doSelectByVisibleText(self, locator, text):
        s = Select(locator)
        s.select_by_visible_text(text)

    def doSelectByIndex(self, locator, index):
        s = Select(locator)
        s.select_by_index(index)

    def waitForSomeTime(self, millisecond):
        try:
            time.sleep(millisecond)
        except Exception as e:
            print(e.message)

    def pageScrollTillEnd(self):
        scroll_pause_time = 0.5
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(scroll_pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def dragAndDrop(self, source_ele, target_ele):
        try:
            act = ActionChains(self.driver)
            act.drag_and_drop(source_ele, target_ele)
        except Exception as e:
            print(e.message)

    def mouseHover(self, element):
        try:
            act = ActionChains(self.driver)
            act.move_to_element(element)
        except Exception as e:
            print(e.message)

    def doDoubleClick(self, element):
        try:
            act = ActionChains(self.driver)
            act.double_click(element)
        except Exception as e:
            print(e.message)

    def waitUntilElementToBeClickable(self, locator):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.visibility_of_element_located(locator)).click()
        except Exception as e:
            print(e.message)

    def get_element_text(self, locator):
        try:
            wait = WebDriverWait(self.driver, 20)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            print(e.message)
    def is_element_visible(self,locator):
        try:
            wait=WebDriverWait(self.driver,20)
            element=wait.until(EC.visibility_of_element_located(locator))
            return bool(element)
        except Exception as e:
            print(e.message)

