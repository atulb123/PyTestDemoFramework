from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import pytest
from pages.LoginPage import LoginPage
from utils.ReadJson import ReadJson


class Test_Login:
    @pytest.mark.smoke
    def test_verifytTitle(self,setup):
        self.driver,self.wait=setup
        assert self.wait.until(expected_conditions.title_is('Your store. Login'))

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_verifyLogin(self,setup):
        self.driver, self.wait = setup
        loginPage=LoginPage(self.driver,self.wait)
        userType=ReadJson.getUserData("User Type 1")
        loginPage.enterTextToTextBox(LoginPage.userNameTextBox,userType.get('userName'))
        loginPage.enterTextToTextBox(LoginPage.passwordTextBox,userType.get('password'))
        loginPage.clickElement(LoginPage.loginButton)
        loginPage.clickElementByJavaScript(LoginPage.logoutButton)
        assert self.wait.until(expected_conditions.title_is('Your store. Login')),"Login Failed"




