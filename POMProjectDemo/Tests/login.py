from selenium import webdriver
import time
import unittest
import HtmlTestRunner
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
import sys
from webdriver_manager.chrome import ChromeDriverManager
sys.path.append('D:\\SQL\\POMProjectDemo')



from POMProjectDemo.Pages.homePage import HomePage
from POMProjectDemo.Pages.loginPage import LoginPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/Warid Hasan/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(29)
        cls.driver.maximize_window()

    def test_01_login_vaild(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username('Admin')
        login.enter_password('admin123')
        login.click_login()
 
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
    

    def test_02_login_invaild_username(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(driver)
        login.enter_username('Admin1')
        login.enter_password('admin123')
        login.click_login()
        message = driver.find_element('xpath').text()
        self.assertEqual(message, "Invalid credentials333")


        # self.driver.find_element("name", "username").send_keys("Admin")
        # self.driver.find_element("name", "password").send_keys("admin123")
        # self.driver.find_element("xpath", '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # self.driver.find_element("xpath", '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li').click()
        # self.driver.find_element("xpath", '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
        time.sleep(25)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Complete, Please Check Carefully")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='POMProjectDemo/Reports'))

    