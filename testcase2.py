from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")


#TEST CASE 2

driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(11) > a').click()
dropdown = driver.find_element(By.ID, "dropdown")
select = Select(dropdown)
chose_option=select.select_by_value("2")
selected_option = select.first_selected_option
if selected_option.text == "Option 2":
    print("2 is selected!")
else:
    print("2 is not selected.")
driver.back()
driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(36) > a').click()
driver.close()



sleep(12)

