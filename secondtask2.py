#3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

class Main(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(5)
        cookies = self.driver.get_cookies()
        print(cookies)


    def test_Download(self):
        self.driver.find_element(By.LINK_TEXT, "File Download").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.LINK_TEXT, "some-file.txt").click()
        self.driver.implicitly_wait(5)



    def close_WD(self) -> None:
        self.driver.close()