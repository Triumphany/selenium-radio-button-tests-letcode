from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("Chrome_driver_location")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://letcode.in/radio")

Going = driver.find_element(By.XPATH, "//input[@id='going']")
Not_Going = driver.find_element(By.XPATH, "//input[@id='notG']")
Maybe = driver.find_element(By.XPATH, "//input[@id='maybe']")

def Going_enable_check():
    if Going.is_enabled():
        print("Going: enabled")
    else:
        print("Going test: failed")

def Not_Going_check():
    if Not_Going.is_enabled():
        print("Not Going: enabled")
    else:
        print("Not Going test: failed")

def Maybe_check():
    if not Maybe.is_enabled():
        print("Maybe test: pass")
    else:
        print("Maybe box still enabled: test failed")

Going_enable_check()
Not_Going_check()
Maybe_check()

driver.quit()