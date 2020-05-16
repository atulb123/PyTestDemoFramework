from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.BasePage import BasePage


class LoginPage(BasePage):
    userNameTextBox = (By.ID,'Email')
    passwordTextBox = (By.ID,'Password')
    loginButton = (By.XPATH,"//input[@value='Log in']")
    logoutButton = (By.XPATH,"//a[.='Logout']")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
