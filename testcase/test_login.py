import pytest
from pages.LoginPage import Login


@pytest.mark.usefixtures("setup")
class TestDemo:
    def test_demo(self):
        lp=Login(self.driver)
        lp.clearValueFromText()
        lp.enterValueInText()
        lp.clearValueFromPasswordFields()
        lp.clearValueFromPasswordFields()
        lp.clickLoginButton()



