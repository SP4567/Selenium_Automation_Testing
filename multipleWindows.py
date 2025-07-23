import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class multiSelect:
    def demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent = driver.current_window_handle
        print(parent)
        driver.find_element(By.XPATH, "//span[@class='style_cross__q1ZoV']//img[@alt='cross']").click()
        driver.find_element(By.XPATH, "//div[@class='MuiStack-root css-v1gwbx']").click()
        allHandles = driver.window_handles
        print(allHandles)
        for handles in allHandles:
            if handles != parent:
                driver.switch_to.window(handles)
                driver.find_element(By.XPATH, "//input[@id='email']").send_keys('yoyo')
                time.sleep(5)
                driver.close()
                break
        driver.switch_to.window(parent)
        time.sleep(7)
obj = multiSelect()
obj.demo()