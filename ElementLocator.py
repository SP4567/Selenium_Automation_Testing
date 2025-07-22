import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriver

class FindElementByID():
    def locate_by_id(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys("suyashpandey9611@gmail.com")
        # driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("suyashpandey9611@gmail.com")
        # driver.find_element(By.PARTIAL_LINK_TEXT, "Book & Manage your Busines").click()
        print(len(driver.find_elements(By.TAG_NAME, "input")))
        list = driver.find_elements(By.TAG_NAME, "a")
        for i in list:
            print(i.text)
        # driver.find_element(By.ID, "your_value").send_keys("value")
findById = FindElementByID()
findById.locate_by_id()
time.sleep(20)