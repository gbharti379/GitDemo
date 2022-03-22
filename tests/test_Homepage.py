import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObject.HomePage import HomePage
from testData.test_HomePage import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getname().send_keys(getData[0])
        log.info("Getting the name : "+getData[0])
        homepage.getEmail().send_keys(getData[1])
        homepage.getPassword().send_keys(getData[2])
        self.selectOptionbyText(homepage.getDrop(), getData[3])

        homepage.getsubmitButton().click()
        submit = homepage.getSubmitText().text
        if 'Success' in submit:
            log.info("You got it")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepagedata)
    def getData(self, request):
        return request.param