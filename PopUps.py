import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class popUpsDemo:
    def demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        time.sleep(4)
obj = popUpsDemo()
obj.demo()