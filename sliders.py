import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class popUpsDemo:
    def demo(self):
        driver = webdriver.Chrome()
        driver.get("https://www.snapdeal.com/products/electronics-home-audio-systems?sort=plrty&q=Price%3A1408%2C1935%7C")
        chains = ActionChains(driver)
        demo1 = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        demo2 = driver.find_element(By.XPATH, "//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        # ActionChains(driver).click_and_hold(demo1).pause(1).move_by_offset(50, 0).release().perform()
        # ActionChains(driver).move_to_element(demo1).click_and_hold(demo2).move_by_offset(80, 0).release().perform()
        ActionChains(driver).drag_and_drop_by_offset(demo1, 100, 0).drag_and_drop_by_offset(demo2, -100, 0).perform()
        time.sleep(15)
obj = popUpsDemo()
obj.demo()