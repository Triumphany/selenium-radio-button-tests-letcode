from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

serv_obj = Service("Chrome_driver_location")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://letcode.in/radio")

Foo = driver.find_element(By.XPATH, "//input[@id='foo']")
bar = driver.find_element(By.XPATH, "//input[@id='notfoo']")

def foo_selection():
    if Foo.is_selected():
        print("Foo is selected")
    else:
        print("Foo is not selected")

def bar_selection():
    if bar.is_selected():
        print("Bar is selected")
    else:
        print("bar is not selected")


foo_selection()
bar_selection()

driver.quit()
