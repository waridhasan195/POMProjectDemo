class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.wecome_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li'
        self.logout_link_xpath = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def click_welcome(self):
        self.driver.find_element('xpath', self.wecome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element('xpath',self.logout_link_xpath).click()

        