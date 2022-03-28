import time

from selenium import webdriver
from selenium.webdriver.common.by import By


from CoreFramework.CommonWebAction import CommonWebAction

class Login(CommonWebAction):

    username_id="Email"
    password_id="Password"
    login_xpath="//div/button[text()='Log in']"
    logout_xpath="//li/a[text()='Logout']"


    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def clearValueFromText(self):
        self.clearValueFromTextBox(By.ID,self.username_id)

    def enterValueInText(self):
        self.enterValueInTextBox(By.ID,self.username_id,"admin@yourstore.com")

    def clearValueFromPasswordFields(self):
        self.clearValueFromTextBox(By.ID,self.password_id)

    def enterValueInPasswordFields(self):
        self.enterValueInTextBox(By.ID,self.password_id,"admin")

    def clickLoginButton(self):
        self.clickOnElement(By.XPATH,self.login_xpath)
        time.sleep(10)








