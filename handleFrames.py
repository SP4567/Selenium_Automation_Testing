import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class IFrameDemo:
    def demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target")
        driver.maximize_window()
        time.sleep(3)  # Let page load
        # Switch to main iframe where the result is shown
        driver.switch_to.frame("iframeResult")
        time.sleep(2)
        # Now interact with the link inside the iframe
        res = driver.find_element(By.XPATH, "//a[normalize-space()='W3Schools.com']")
        res.click()
        # This will open W3Schools in the same iframe
        time.sleep(3)
        # There is another iframe nested inside - we must switch to that!
        inner_iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(inner_iframe)
        # Now click the CSS Tutorial link inside the inner iframe
        css_link = driver.find_element(By.XPATH, "//a[@title='CSS Tutorial'][normalize-space()='CSS']")
        css_link.click()
        time.sleep(10)
        driver.quit()
obj = IFrameDemo()
obj.demo()
