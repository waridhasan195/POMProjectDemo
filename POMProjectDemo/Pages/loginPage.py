import sys
sys.path.append('D:\\SQL\\POMProjectDemo')

from POMProjectDemo.Locators.locators import Locators

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath
        self.invaildUsername_message_xpath = Locators.invalid_xpath

    def enter_username(self, username):
        self.driver.find_element('name', self.username_textbox_name).clear()
        self.driver.find_element('name', self.username_textbox_name).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element('name', self.password_textbox_name).clear()
        self.driver.find_element('name', self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element('xpath', self.login_button_xpath).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element('xpath', self.invaildUsername_message_xpath).text()
        return msg
