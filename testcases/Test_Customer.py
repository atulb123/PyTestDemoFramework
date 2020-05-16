import random, string, pytest
from selenium.webdriver.support import expected_conditions
from pages.CustomerPage import CustomerPage
from pages.LoginPage import LoginPage
from utils.ReadJson import ReadJson
class Test_Customer:
    @pytest.mark.regression
    def test_verifyCreateCustomer(self, setup):
        self.driver, self.wait = setup
        customerPage = CustomerPage(self.driver, self.wait)
        userType = ReadJson.getUserData("User Type 1")
        loginPage = LoginPage(self.driver, self.wait)
        loginPage.enterTextToTextBox(LoginPage.userNameTextBox, userType.get('userName'))
        loginPage.enterTextToTextBox(LoginPage.passwordTextBox, userType.get('password'))
        loginPage.clickElement(LoginPage.loginButton)
        customerPage.clickElement(customerPage.registetedCustomerLink)
        customerPage.clickElement(customerPage.addNewButton)
        customerPage.enterTextToTextBox(customerPage.email_textbox, userType.get('userName') + ''.join(
            random.choice(string.ascii_letters) for x in range(3)))
        customerPage.enterTextToTextBox(customerPage.password_textbox, userType.get('password'))
        customerPage.enterTextToTextBox(customerPage.firstName_textbox, userType.get('firstName'))
        customerPage.enterTextToTextBox(customerPage.lastName_textbox, userType.get('lastName'))
        customerPage.clickElement(customerPage.gender_radio)
        customerPage.moveToElementandClick(customerPage.calender_icon)
        customerPage.moveToElementandClick(customerPage.currentDate)
        customerPage.selectFromDropDown(customerPage.vendor_dropdown, userType.get('vendor'))
        customerPage.clickElement(customerPage.saveButton)
        assert self.wait.until(expected_conditions.visibility_of_element_located(
            customerPage.customerCreatedSuccessMessage)).is_displayed(), "Customer was not created"
