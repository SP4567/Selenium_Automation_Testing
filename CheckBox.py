import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkbox:
    def checkBox(self):
        driver = webdriver.Chrome()
        driver.get("https://www.sugarcrm.com/au/request-demo/?utm_medium=organic&utm_source=google.com&utm_source=google.com&utm_medium=organic")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//label[@for='input_1_12_1']").click()
        select = driver.find_element(By.XPATH, "//label[@for='input_1_12_1']").is_selected()
        print(select)
        time.sleep(10)
obj = Checkbox()
obj.checkBox()
