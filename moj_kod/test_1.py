import unittest
from datetime import time
from selenium import webdriver



class TestWSB(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver1 = webdriver.Chrome(executable_path=r'C:\driver_selenium\ChromeDrive_73\chromedriver.exe')
        self.driver2 = webdriver.Firefox(executable_path=r'C:\driver_selenium\FirefoxDrive_24\geckodriver.exe')

    # @unittest.skip('nie bedzie uruchomianie')
    def test_windows_ff(self):
        driver1 = self.driver1
        driver1.maximize_window()
        #driver1.set_window_size(800, 600,)
        #driver1.minimize_window()

    def test_windows_ch(self):
        driver2 = self.driver2
        driver2.maximize_window()
        # driver2.set_window_size(800, 600,)
        # driver2.minimize_window()

    def test_redirect_ff(self):
        driver1 = self.driver1
        driver1.get('http://www.google.pl/')
        self.assertIn('Google', driver1.title, msg=None)
        #time.sleep(10)

    def test_redirect_ch(self):
        driver2 = self.driver2
        driver2.get( 'http://www.onet.pl/')
        self.assertIn('Onet – Jesteś na bieżąco', driver2.title, msg=None)
        #time.sleep(10)

    @classmethod
    def tearDownClass(self):
        self.driver1.close()
        self.driver2.close()


if __name__ == '__main__':
    unittest.main()

