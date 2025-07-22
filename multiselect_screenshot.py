import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MultiselectDropDown:
    def multiselect(self):
        driver = webdriver.Chrome()
        driver.get("https://getbootstrap.com/docs/5.0/forms/select/")
        driver.maximize_window()
        demo = driver.find_element(By.XPATH, "//select[@aria-label='Default select example']")
        sle = Select(demo)
        sle.select_by_index(0)
        time.sleep(2)
        sle.select_by_index(1)
        time.sleep(2)
        sle.select_by_index(2)
        time.sleep(2)
        sle.select_by_index(3)
        time.sleep(2)
        sle.select_by_value("1")
        time.sleep(2)
        sle.select_by_value("2")
        time.sleep(2)
        sle.select_by_value("3")
        time.sleep(5)
        driver.get_screenshot_as_file('screenshot.png')
        driver.get_screenshot_as_base64()
obj = MultiselectDropDown()
obj.multiselect()
