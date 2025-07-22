import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class HiddenElements(object):
    def elementState(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element)
        time.sleep(2)
obj = HiddenElements()
obj.elementState()