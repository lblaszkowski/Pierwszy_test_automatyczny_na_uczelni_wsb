import os
import unittest
from selenium import webdriver



class TestWSB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #self.driver = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        self.driver = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')

    def test_windows(self):
        driver = self.driver
        driver.maximize_window()

    def test_redirect(self):
        driver = self.driver
        driver.get('http://www.onet.pl/')
        self.assertIn('Onet – Jesteś na bieżąco', driver.title, msg=None)
        main_page = driver.current_window_handle
        # driver.execute_script("$(window.open(''))")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get('http://www.wp.pl/')
        # driver.get_screenshot_as_file(os.getcwd()+'\\'+'1.png') //
        driver.get_screenshot_as_file('C:/Pierwszy_test_automatyczny_na_uczelni_wsb/moj_kod/folder_test_2/img/'+'1.png')
        driver.switch_to.window(main_page)
        driver.execute_script("window.open('');")
        # driver.execute_script("$(window.open(''))")
        driver.switch_to.window(driver.window_handles[2])
        driver.get('http://www.google.pl/')
        # driver.get_screenshot_as_file(os.getcwd() + '\\' + '2.png')
        driver.get_screenshot_as_file('C:/Pierwszy_test_automatyczny_na_uczelni_wsb/moj_kod/folder_test_2/img/'+'2.png')
        driver.switch_to.window(main_page)
        driver.execute_script("window.open('');")
        # driver.execute_script("$(window.open(''))")
        driver.switch_to.window(driver.window_handles[3])
        driver.get('http://www.google.pl/')
        # driver.get_screenshot_as_file(os.getcwd() + '\\' + '3.png')
        driver.get_screenshot_as_file('C:/Pierwszy_test_automatyczny_na_uczelni_wsb/moj_kod/folder_test_2/img/'+'3.png')
        driver.switch_to.window(main_page)
        # driver.get_screenshot_as_file(os.getcwd() + '\\' + '0.png')
        driver.get_screenshot_as_file('C:/Pierwszy_test_automatyczny_na_uczelni_wsb/moj_kod/folder_test_2/img/'+'0.png')


    @classmethod
    def tearDownClass(self):
        #self.driver.close() # zamyka ostatne aktywne okno
        self.driver.quit() # zamyka przegladarke po tescie


if __name__ == '__main__':
    unittest.main()
