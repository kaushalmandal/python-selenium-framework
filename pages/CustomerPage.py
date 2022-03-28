from selenium.webdriver.common.by import By
from CoreFramework.CommonWebAction import CommonWebAction
from utilities import XLUtil
from utilities.LoggerUtil import Utils


class Customer(CommonWebAction):
    log=Utils.customLogger()
    customer_header = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    customer_text = "(//li//a/p[contains(text(),' Customers')])[1]"
    add_new_button = "//a[@href='/Admin/Customer/Create']"
    email_text_xpath = "//input[@id='Email']"
    password_text_xpath = "//input[@id='Password']"
    firstname_text_xpath = "//input[@id='FirstName']"
    lastname_text_xpath = "//input[@id='LastName']"
    gender_male_xpath = "//input[@id='Gender_Male']"
    dob_text_xpath = "//input[@id='DateOfBirth']"
    company_text_xpath = "//input[@id='Company']"
    tax_exempt_xpath = "//input[@id='IsTaxExempt']"
    customer_role_xpath = "//input[@aria-labelledby='SelectedCustomerRoleIds_label']"
    customer_role_administrator_xpath = "//li[text()='Administrators']"
    admin_Comment_xpath = "//div/textarea[@id='AdminComment']"

    path = "D:\PythonSeleniumPrrojectrs\TestData\customer.xlsx"
    rows = XLUtil.getColumnCount(path, "Sheet1")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def clickOnCustomerLink(self):
        self.clickOnElement(By.XPATH, self.customer_header)


    def clickOnCutomerText(self):
        self.clickOnElement(By.XPATH, self.customer_text)


    def clickOnAddNewButton(self):
        self.clickOnElement(By.XPATH, self.add_new_button)


    def enterValueInEmailFields(self):
        self.log.info('Enter value in email fields')
        # self.enterValueInTextBox(By.XPATH, self.email_text_xpath, "kaushal.mandal000@gmail.com")
        self.enterValueInTextBox(By.XPATH, self.email_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 1))


    def enterValueInPAsswordFields(self):
        self.log.info('Enter value in password fields')
        self.enterValueInTextBox(By.XPATH, self.password_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 2))


    def enterValueInFirstNameFields(self):
        self.log.info('Enter value in firstname fields')
        self.enterValueInTextBox(By.XPATH, self.firstname_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 3))


    def enterValueInLastNameFields(self):
        self.log.info('Enter value in lastname fields')
        self.enterValueInTextBox(By.XPATH, self.lastname_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 4))


    def clickOnGenderRadioButton(self):
        self.clickOnElement(By.XPATH, self.gender_male_xpath)


    def enterValueInDOBText(self):
        self.log.info('Enter value in DOB fields')
        self.enterValueInTextBox(By.XPATH, self.dob_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 5))


    def enterValueInCompanyText(self):
        self.log.info('Enter value in company text')
        self.enterValueInTextBox(By.XPATH, self.company_text_xpath, XLUtil.readData(Customer.path, "Sheet1", 2, 6))


    def clickCheckBoxTaxExempt(self):
        self.clickOnElement(By.XPATH, self.tax_exempt_xpath)


    def clickCustomerRoleTextBox(self):
        self.clickOnElement(By.XPATH, self.customer_role_xpath)


    def clickCustomerRoleAdministrator(self):
        self.clickOnElement(By.XPATH, self.customer_role_administrator_xpath)


    def enterValueInAdminComment(self):
        self.log.info('Enter value in admin comment')
        self.enterValueInTextBox(By.XPATH, self.admin_Comment_xpath, "admin-comment")
