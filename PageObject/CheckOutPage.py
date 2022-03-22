from selenium.webdriver.common.by import By

from PageObject.Confirm import ConfirmPage


class CheckOutPage:

    def __init__(self , driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardfooter = (By.CSS_SELECTOR, ".card-footer button")
    checkoutbtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutFinal = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardfooter)

    def getCheckOut(self):
        return self.driver.find_element(*CheckOutPage.checkoutbtn)

    def getCheckOutFinal(self):
        self.driver.find_element(*CheckOutPage.checkOutFinal).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage