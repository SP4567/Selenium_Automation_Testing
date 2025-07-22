import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# Disable notifications
chrome_options.add_argument("--disable-notifications")
# Disable geolocation prompts
chrome_options.add_argument("--disable-geolocation")
# Allow fake UI for media streams (e.g., microphone/camera access)
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--disable-ads")
# Alternatively, use preferences for more granular control (e.g., allow notifications)
prefs = {"profile.default_content_setting_values.notifications": 1} # 1 for allow, 2 for block
chrome_options.add_experimental_option("prefs", prefs)
class handleDates:
    def Dates(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.makemytrip.com/")
        # driver.find_element(By.XPATH, "//span[@class='commonModal__close']").click()
        from_city = driver.find_element(By.ID, "fromCity")
        from_city.click()
        city = driver.find_element(By.XPATH, "//input[@placeholder='From']")
        city.send_keys("New Delhi")
        city.send_keys(Keys.ENTER)
        from_city = driver.find_element(By.XPATH, "//span[normalize-space()='To']")
        from_city.click()
        city2 = driver.find_element(By.XPATH, "//input[@placeholder='To']")
        city2.send_keys("New York")
        city.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "(//label[@for='departure'])[1]").click()
        driver.find_element(By.XPATH, "//div[@aria-label='Thu Jul 31 2025']//div[@class='dateInnerCell']").click()
        time.sleep(200)
obj = handleDates()
obj.Dates()
