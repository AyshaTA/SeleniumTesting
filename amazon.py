import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
try:
    driver.get("https://www.amazon.in/")
    time.sleep(5)
    check_element=driver.find_element(By.ID,"twotabsearchtextbox")
    check_element.send_keys("iphone16")
    time.sleep(5)
    check_element.send_keys(Keys.ENTER)
    time.sleep(5)
finally:
    driver.quit()

