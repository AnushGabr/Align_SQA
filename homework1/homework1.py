from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.demoblaze.com/")

#task-1

#the code is on drivers.py

#task---2
class HeaderElementsExistence():

    def find_home_elem_in_header(self):
        home = driver.find_element(By.XPATH, "//*[contains(text(),'Home')]")
        if home:
            print('Element is found')
        else:
            print('No such element')

    def find_contact_elem_in_header(self):
        contact = driver.find_element(By.XPATH, "//a[@class='nav-link' and @data-target= '#exampleModal']")
        print('Element is found' if contact else 'No such element')

    def is_about_us_element_exist(self):
        about_us = driver.find_element(By.XPATH, "//a[text() = 'About us']")
        if about_us:
            print('element is located')
        else:
            print('No such element')

    def is_cart_elem_exist(self):
        cart = driver.find_element(By.XPATH, "//a[@id='cartur']")
        print('Element is located' if cart else 'No such element')

    def finding_path_for_login(self):
        login = driver.find_element(By.XPATH, "//*[contains(@id, 'logInModalLabel')]")
        print('Element is found' if login else 'No such element')

    def is_sign_up_elem_exist(self):
        sign_up = driver.find_element(By.XPATH, "//a[@id= 'signin2']")
        print('Element is found' if sign_up else 'No such element')


#task----3

def find_cat_elements():
    cat_elements_list = driver.find_elements(By.CSS_SELECTOR, "#itemc")
    print('Element is found' if cat_elements_list[0] else 'No such element')
    print('Element is found' if cat_elements_list[1] else 'No such element')
    print('Element is found' if cat_elements_list[2] else 'No such element')




#task----4

def finding_highest_price_of_products_in_first_page():
    driver.implicitly_wait(12)
    product_divs_list = driver.find_elements(By.CSS_SELECTOR, 'div[id = "tbodyid"] > div')
    products = {}

    for div in product_divs_list:
        product_name = div.find_element(By.CSS_SELECTOR, 'a[class="hrefch"]').get_attribute("innerText")
        product_price_in_string = div.find_element(By.CSS_SELECTOR, 'h5').get_attribute('innerText')
        price_in_num = float(product_price_in_string[1::])
        products[product_name] = price_in_num

    max_price = max(products.values())

    for name in products:
        if max_price == products[name]:
            print(name,products[name])

