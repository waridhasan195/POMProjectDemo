import sys
sys.path.append('D:\\SQL\\POMProjectDemo')

from POMProjectDemo.Locators.locators import Locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.wecome_link_xpath = Locators.wecome_link_xpath
        self.logout_link_xpath = Locators.logout_link_xpath

    def click_welcome(self):
        self.driver.find_element('xpath', self.wecome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element('xpath',self.logout_link_xpath).click()

        