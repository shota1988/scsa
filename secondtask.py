from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest

#1
class Main(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://the-internet.herokuapp.com/")

    def test_adding_elements(self):
        self.driver.find_element(By.LINK_TEXT, "Add/Remove Elements").click()
        button=self.driver.find_element(By.XPATH, '//*[@id="content"]/div/button')
        for i in range(10):
            button.click()
        self.driver.implicitly_wait(5)
        for j in range(1,8):
            j=1
            del_button = self.driver.find_element(By.XPATH, f'//*[@id="elements"]/button{[j]}')
            del_button.click()
            self.driver.implicitly_wait(2)
        remaining_element = self.driver.find_elements(By.XPATH, '//*[@id="elements"]/button')
        if len(remaining_element)==3:
            print("remaining_element is 3, as Excepted")
        else:
            print("remaining_element is not 3")

    def close_WD(self) -> None:
        self.driver.close()

