from selenium.webdriver.common.by import By

from CoreFramework.CommonWebAction import CommonWebAction


class ContentManagement(CommonWebAction):
    content_mgmt_xpath = "//li/a/p[contains(text(),'Content management')]"
    new_item_xpath = "//li/a/p[contains(text(),' News items')]"
    add_new_xpath = "//a[@href='/Admin/News/NewsItemCreate']"
    title_xpath = "//input[@id='Title']"
    short_desc_xpath = "//div/textarea[@id='Short']"
    start_date_xpath = "//input[@id='StartDateUtc']"
    end_date_xpath = "//input[@id='EndDateUtc']"
    limited_to_store_xpath = "//div[@role='listbox']"
    limited_to_store_value_xpath = "//li[text()='Test store 2']"
    frame_xpath = "//iframe[@id='Full_ifr']"
    full_desc_xpath = "//body[@id='tinymce']"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def clickOnContentMgmt(self):
        self.clickOnElement(By.XPATH, self.content_mgmt_xpath)

    def clickOnNewItem(self):
        self.clickOnElement(By.XPATH, self.new_item_xpath)

    def clickOnAddNew(self):
        self.clickOnElement(By.XPATH, self.add_new_xpath)

    def enterValueInTitle(self):
        self.enterValueInTextBox(By.XPATH, self.title_xpath, "new item")

    def enterValueInShortDesc(self):
        self.enterValueInTextBox(By.XPATH, self.short_desc_xpath, "Add new item in content management")

    def enterValueInStartDapte(self):
        self.enterValueInTextBox(By.XPATH, self.start_date_xpath, "20/03/2022")

    def enterValueInEndDate(self):
        self.enterValueInTextBox(By.XPATH, self.end_date_xpath, "25/03/2022")

    def clickOnLimitedToStore(self):
        self.clickOnElement(By.XPATH, self.limited_to_store_xpath)
        self.clickOnElement(By.XPATH, self.limited_to_store_value_xpath)

    def switchFrame(self):
        self.switchToFrame(self.frame_xpath)

    def enterValueInFullDesc(self):
        self.enterValueInTextBox(By.XPATH, self.full_desc_xpath, "product desc are here")

