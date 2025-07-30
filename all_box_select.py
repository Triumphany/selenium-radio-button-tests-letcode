from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("Chrome_driver_location")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://letcode.in/radio")
checkboxs = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(checkboxs))

for radio_box in checkboxs:
    if not radio_box.is_selected():
        radio_box.click()
driver.quit()