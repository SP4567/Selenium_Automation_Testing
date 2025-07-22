import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkbox:
    def checkBox(self):
        driver = webdriver.Chrome()
        driver.get("https://designsystem.digital.gov/components/radio-buttons/")
        driver.maximize_window()
        driver.find_element(By.XPATH, "//label[@for='historical-douglass'] | //label[@for='historical-washington']").click()
        # driver.find_elements(By.XPATH, "//label[@for='historical-douglass'] | //label[@for='historical-washington']")
        sle = driver.find_element(By.XPATH,"//label[@for='historical-douglass'] | //label[@for='historical-washington']").is_selected()
        print(sle)
        time.sleep(10)
obj = Checkbox()
obj.checkBox()
