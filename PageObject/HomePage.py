from selenium.webdriver.common.by import By

from PageObject.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    drop = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    submitText = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def shopitem(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getDrop(self):
        return self.driver.find_element(*HomePage.drop)

    def getsubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getSubmitText(self):
        return self.driver.find_element(*HomePage.submitText)
