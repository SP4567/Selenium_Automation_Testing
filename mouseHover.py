import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class popUpsDemo:
    def demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onmouseover")
        driver.switch_to.frame("iframeResult")
        chains = ActionChains(driver)
        demo = driver.find_element(By.XPATH, "//img[@alt='Smiley']")
        time.sleep(5)
        chains.move_to_element(demo).perform()
        time.sleep(15)
obj = popUpsDemo()
obj.demo()