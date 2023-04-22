#2
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
import unittest

class Main(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(5)

    def test_Dynamic_Content(self):
        self.driver.find_element(By.LINK_TEXT, "Dynamic Content").click()
        text_element1 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]')
        #print("N1 "text_element.text)
        self.driver.refresh()
        text_element2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]')
        #print("N2 "+text_element1.text)
        if text_element2!=text_element1:
            print("it was refreshed")


    def close_WD(self) -> None:
        self.driver.close()
