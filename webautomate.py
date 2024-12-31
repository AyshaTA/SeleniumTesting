import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
try:
    driver.get("http://127.0.0.1:5500/index.html")
    time.sleep(3)
    check_element=driver.find_element(By.TAG_NAME,"h2")
    if check_element.text.strip()=="FISAT":
        nameTextBox=driver.find_element(By.NAME,"Name")
        nameTextBox.send_keys("Aysha")
        time.sleep(3)

        print("Test PASSED")
    else:
        print("Test Failed")
finally:
    driver.quit()
    
