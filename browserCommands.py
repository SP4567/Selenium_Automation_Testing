import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Commands:
    def seleniumCommands(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/search?q=google+careers+india&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQsyOTg2NzAxajBqMagCCLACAfEF6HIJyr5ruu4&sourceid=chrome&ie=UTF-8&jbr=sep:0")
        # driver.maximize_window()
        # driver.minimize_window()
        # print(driver.title)
        # print(driver.current_url)
        # driver.fullscreen_window()
        # driver.refresh()
        # driver.forward()
        # driver.back()
        # driver.quit()
obj = Commands()
obj.seleniumCommands()
time.sleep(200)