import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class ElementState:
    def checkState(self):
        driver = webdriver.Chrome()
        driver.get("https://training.openspan.com/login")
        state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("suyashpandey")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("hello@babybye")
        state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state)
        time.sleep(4)
obj = ElementState()
obj.checkState()