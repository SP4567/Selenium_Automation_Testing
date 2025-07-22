import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.drivers.chrome import ChromeDriver

chrome_options = Options()
chrome_options.add_argument("--diable-notifications")

class AutoSuggest:
    def suggest(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        # driver.maximize_window()
        driver.find_element(By.XPATH, "//span[@class='style_cross__q1ZoV']//img[@alt='cross']").click()
        dd = driver.find_element(By.XPATH, "//p[normalize-space()='DEL, Indira Gandhi International']")
        dd.click()
        dd_ = driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-92q1lr']//div[1]//div[1]")
        time.sleep(2)
        dd_.send_keys("New Delhi")
        time.sleep(2)
        dd_.send_keys(Keys.ENTER)
        driver.get_screenshot_as_file('screenshot.png')
        driver.get_screenshot_as_base64()
        time.sleep(100)
obj = AutoSuggest()
obj.suggest()