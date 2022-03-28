import time

from pages.ContentManagement import ContentManagement
import pytest
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestContentManagement:
    def test_content(self):
        c = ContentManagement(self.driver)
        time.sleep(3)
        c.clickOnContentMgmt()
        time.sleep(3)
        c.clickOnNewItem()
        time.sleep(3)
        c.clickOnAddNew()
        time.sleep(3)
        c.enterValueInTitle()
        time.sleep(3)
        c.enterValueInShortDesc()
        time.sleep(3)
        self.driver.switch_to.frame("Full_ifr")
        #c.switchFrame()
        time.sleep(3)
        c.enterValueInFullDesc()
        time.sleep(3)
        self.driver.switch_to.default_content()
        c.enterValueInStartDapte()
        time.sleep(3)
        c.enterValueInEndDate()
        time.sleep(3)
        c.clickOnLimitedToStore()
        time.sleep(3)
