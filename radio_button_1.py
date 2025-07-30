from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("Chrome_driver_location")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://letcode.in/radio")

select_any_one = driver.find_element(By.XPATH, "//input[@id='yes']")
select_any_one.click()

if select_any_one.is_selected():
    print("Radio button 'Yes' is selected ✅")
else:
    print("Radio button 'Yes' is NOT selected ❌")

driver.quit()