from selenium import webdriver
import time
import unittest
from C:Users\Gaurav\PycharmProjects\selenium_test\PageOfModel Project import LoginPage
from PageOfModel.Pages.HomePage.py import Homepage


class logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\Users\\Gaurav\\Downloads\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)



        #self.driver.get("https://opensource-demo.orangehrmlive.com/")
        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #self.driver.implicitly_wait(10)
        #self.driver.find_element_by_id("welcome").click()
        #self.driver.find_element_by_link_text("Logout").click()
        #self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__=='__main__':
    unittest.main()