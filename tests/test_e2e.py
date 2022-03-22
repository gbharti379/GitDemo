import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopitem()
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            log.info(card.text)
            i = i + 1
            cardText = card.text
            if cardText == "Blackberry":
                # log.info("Checking the Product based on name")
                checkOutPage.getCardFooter()[i].click()
                checkOutPage.getCheckOut().click()
        confirmPage = checkOutPage.getCheckOutFinal()

        # --------------------Confirm page------------------------

        confirmPage.getcountrybox().send_keys("India")
        log.info("Selecting the Country name India")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "suggestions")))
        suggestions = confirmPage.chooseCounty()
        for suggest in suggestions:
            if suggest.text == "India":
                suggest.click()
        confirmPage.getCheckBox().click()
        confirmPage.getPurchaseButton().click()
        success = confirmPage.getSuccessMessage().text
        assert "Success! Thank you!" in success
        log.info("Capturing Screenshot")
        self.driver.get_screenshot_as_file("screen.png")
