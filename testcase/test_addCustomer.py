import time

import pytest

from pages.CustomerPage import Customer


@pytest.mark.usefixtures("setup")
class TestAddCustomer:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.c = Customer(self.driver)

    def test_add_customer(self):
        time.sleep(10)
        self.c.clickOnCustomerLink()
        time.sleep(3)
        self.c.clickOnCutomerText()
        time.sleep(3)
        self.c.clickOnAddNewButton()
        time.sleep(3)
        self.c.enterValueInEmailFields()
        time.sleep(3)
        self.c.enterValueInPAsswordFields()
        time.sleep(3)
        self.c.enterValueInFirstNameFields()
        time.sleep(3)
        self.c.enterValueInLastNameFields()
        time.sleep(3)
        self.c.clickOnGenderRadioButton()
        time.sleep(3)
        self.c.enterValueInDOBText()
        time.sleep(3)
        self.c.enterValueInCompanyText()
        time.sleep(3)
        self.c.clickCheckBoxTaxExempt()
        time.sleep(3)
        self.c.clickCustomerRoleTextBox()
        time.sleep(3)
        self.c.clickCustomerRoleAdministrator()
        time.sleep(3)
        self.c.enterValueInAdminComment()
