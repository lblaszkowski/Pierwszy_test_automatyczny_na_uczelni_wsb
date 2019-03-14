from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
import random
import string

class Blazedemo(unittest.TestCase):

    _random = ''.join(random.choices(string.ascii_lowercase, k=6))
    name = 'adamek_'+_random
    company = 'adamek_'+_random
    email = 'adamek'+_random+'@poczta.pl'
    passwd = 'adamek123456'

    @classmethod
    def setUpClass(self):
        # self.driver = webdriver.Chrome(executable_path="E:\\tmp\\selenium\\chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        # self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')

        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get('http://blazedemo.com/register')

    def test_register(self):
        driver = self.driver
        self.assertTrue(driver.find_element_by_class_name('panel-heading').text == 'Register', msg=None)
        driver.find_element_by_id('name').send_keys(self.name)
        driver.find_element_by_id('company').send_keys(self.company)
        driver.find_element_by_id('email').send_keys(self.email)
        driver.find_element_by_id('password').send_keys(self.passwd)
        driver.find_element_by_id('password-confirm').send_keys(self.passwd)
        driver.find_element_by_class_name('btn-primary').click()
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'panel-heading'), 'Login'))

    def test_login_after_register(self):
        driver = self.driver
        self.assertTrue(driver.find_element_by_class_name('panel-heading').text == 'Login', msg=None)
        driver.find_element_by_id('email').send_keys(self.email)
        driver.find_element_by_id('password').send_keys(self.passwd)
        if driver.find_element_by_name('remember').is_displayed():
            driver.find_element_by_name('remember').click()
        driver.find_element_by_class_name('btn-primary').click()

    def test_check_if_login(self):
        driver = self.driver
        body = driver.find_element_by_class_name('panel-body')
        self.assertTrue(body.text == 'You are logged in!')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Blazedemo('test_register'))
    suite.addTest(Blazedemo('test_login_after_register'))
    suite.addTest(Blazedemo('test_check_if_login'))
    return suite

# suite = suite()
#if __name__ == '__main__':
unittest.TextTestRunner().run(suite())
