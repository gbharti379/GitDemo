from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    choosecountry = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    successMsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def getcountrybox(self):
        return self.driver.find_element(*ConfirmPage.country)

    def chooseCounty(self):
        return self.driver.find_elements(*ConfirmPage.choosecountry)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMsg)