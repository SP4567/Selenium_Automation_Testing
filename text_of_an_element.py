import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def find():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/about/careers/applications/jobs/results?location=India")
    attr = driver.find_element(By.XPATH, "(//h4[contains(text(),'Minimum qualifications')])[1]").get_attribute("value_id")
    print(attr)
    time.sleep(40)
    driver.quit()
find()