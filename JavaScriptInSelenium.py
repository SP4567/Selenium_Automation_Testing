import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class JSExecution:
    def demo(self):
        driver = webdriver.Chrome()
        # Open new tab and navigate to URL
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_blank');")
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)  # Wait for page to load (better to use WebDriverWait)
        # Now get the element and click using JS
        demo_element = driver.execute_script("return document.getElementsByTagName('a')[7];")
        if demo_element:
            driver.execute_script("arguments[0].click();", demo_element)
        else:
            print("Element not found!")
        time.sleep(7)
obj = JSExecution()
obj.demo()
