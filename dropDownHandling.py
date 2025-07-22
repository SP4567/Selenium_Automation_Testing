import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DropDown:
    def dropDownHandle(self):
        driver = webdriver.Chrome()
        driver.get("https://www.salesforce.com/in/form/signup/sales-ee/?d=topnav2-btn-ft")
        driver.maximize_window()
        driver.find_element(By.NAME, "UserFirstName").send_keys("Suyash")
        driver.find_element(By.NAME, "UserLastName").send_keys("Pandey")
        driver.find_element(By.NAME, "UserTitle").send_keys("Software Engineer")
        driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()
        dropdown = driver.find_element(By.NAME, "CompanyEmployees")
        sle = Select(dropdown)
        sle.select_by_index(1)
        sle.select_by_visible_text("Employees")
        sle.select_by_value("10")
        time.sleep(110)
obj = DropDown()
obj.dropDownHandle()
