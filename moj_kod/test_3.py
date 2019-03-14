from telnetlib import EC
from unittest.test import suite

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest



class TestWSB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
     self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
     #self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')

    def test_windows(self):
        driver = self.driver
        # driver.maximize_window()

    def test_1register(self):
        driver = self.driver
        driver.get('http://www.blazedemo.com/register')
        polename = driver.find_element_by_id('name')
        polename.clear()
        polename.send_keys("Justyna")
        polecompany = driver.find_element_by_id('company')
        polecompany.clear()
        polecompany.send_keys("policja")
        poleemail = driver.find_element_by_id('email')
        poleemail.clear()
        poleemail.send_keys("janekkolasa121323@currenda.pl")
        polepassword = driver.find_element_by_id('password')
        polepassword.clear()
        polepassword.send_keys("test1234")
        polepassword_confirm = driver.find_element_by_id('password-confirm')
        polepassword_confirm.clear()
        polepassword_confirm.send_keys("test1234")
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/form/div[6]/div/button').click()
        # wait = WebDriverWait(driver, 10)
        # wait.until(EC.text_to_be_present_in_element(driver.find_element__by_class_name('panel-heading').text(),'Login'))


    def test_2login(self):
        driver = self.driver
        driver.get('http://www.blazedemo.com/login')
        # driver.find_element_by_xpath('//*[@id="app-navbar-collapse"]/ul[2]/li[1]').click()
        poleemail = driver.find_element_by_id('email')
        poleemail.clear()
        poleemail.send_keys("janekkolasa121323@currenda.pl")
        polepassword = driver.find_element_by_id('password')
        polepassword.clear()
        polepassword.send_keys("test1234")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[4]/div/button').click()

    @classmethod
    def tearDownClass(self):
        # self.driver.close() #zamyka ostatne aktywne okno
        self.driver.quit() #zamyka przegladarke po tescie

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestWSB('test_1register'))
        suite.addTest(TestWSB('test_2login '))
        return suite

# suite = suite()
# if __name__ == '__main__':
    #unittest.main()
unittest.TextTestRunner().run(suite())