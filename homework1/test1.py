from selenium import webdriver
from wait.wait import Wait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

class Test():

    def __init__(self):
        driver.get("https://www.demoblaze.com/")
        self.get_wait = Wait(driver)
        self.get_wait.wait_for_element_to_be_clickable(By.CSS_SELECTOR, '#itemc')
        self.navigation_elements = driver.find_elements(By.CSS_SELECTOR, '#itemc')

    def is_phones_page_loaded_correctly(self):
        self.navigation_elements[0].click()

        assert self.get_wait.wait_for_element(By.CSS_SELECTOR,".card .img-fluid[src='imgs/HTC_M9.jpg']" ).is_displayed()

    def is_laptops_page_loaded_correctly(self):
        self.navigation_elements[1].click()

        assert self.get_wait.wait_for_element(By.XPATH, "//*[text()='Dell i7 8gb']").is_displayed()

    def is_monitors_page_loaded_correctly(self):
        self.navigation_elements[2].click()

        assert self.get_wait.wait_for_element(By.XPATH, "//*[text()='Apple monitor 24']").is_displayed()


