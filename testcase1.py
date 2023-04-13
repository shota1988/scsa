from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By



#TEST CASE 1.1
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")
try:
    driver.find_element(By.LINK_TEXT, "File Upload").click()
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("C:/Users/shota/Desktop/scsa/qa.png")
    file_input = driver.find_element(By.ID, "file-submit").click()
    result = driver.find_element(By.ID, "content").text
    assert 'File Uploaded!' in result

except: AssertionError:\
    print("not expected result")
sleep(4)
driver.close()


#TEST CASE 1.2
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")

try:
    driver.find_element(By.LINK_TEXT, "File Upload").click()
    file_input = driver.find_element(By.ID, "file-upload")
    file_input.send_keys("C:/Users/shota/Desktop/a.png")
    file_input = driver.find_element(By.ID, "file-submit").click()
    result = driver.find_element(By.ID, "content").text
    assert 'File Uploaded!' in result
except Exception as FileExistsCheck:
    error_message = str(FileExistsCheck)
    if "File not found" in error_message:
        print("File not found. Please provide a valid file path.")
    else:
        print("Other Error occurred")  # other Error which we we are not expecting(wrong url wrong code and etc)
sleep(4)
driver.close()
