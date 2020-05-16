from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.BasePage import BasePage


class CustomerPage(BasePage):
    registetedCustomerLink = (By.XPATH, "(//a[@class='small-box-footer'])[3]")
    email_textbox = (By.ID, 'Email')
    password_textbox = (By.ID, 'Password')
    firstName_textbox = (By.ID, 'FirstName')
    lastName_textbox = (By.ID, 'LastName')
    gender_radio = (By.ID, 'Gender_Male')
    calender_icon = (By.XPATH, "//span[@aria-controls='DateOfBirth_dateview']")
    vendor_dropdown = (By.ID, 'VendorId')
    addNewButton=(By.XPATH,"//a[contains(.,'Add new')]")
    currentDate = (By.XPATH, "//a[.='16']")
    saveButton = (By.XPATH, "//button[@name='save']")
    customerCreatedSuccessMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissable' and contains(.,'new customer has been added')]")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.actions = ActionChains(self.driver)
