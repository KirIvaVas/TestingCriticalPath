from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from math import ceil
from testingParameters import TestFunctions
from exceptions import exc_handler



def driver_options():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver


@exc_handler
def url_composition(driver, catalog_href, products_limit):

    # Catalog route
    category_button = driver.find_element(By.XPATH, catalog_href)
    ActionChains(driver).click(category_button).perform()

    # Products limit. "mse2_limit" goes for particular select.
    select_element = driver.find_element(By.ID, "mse2_limit")
    select = Select(select_element)
    select.select_by_value(products_limit)


@exc_handler
def pages_calc(d, pl):
    products_amount = d.find_element(By.CSS_SELECTOR, "#mse2_totalis").text
    return ceil(int(products_amount) / int(pl))


@exc_handler
def product_search(d, pn):
    return d.find_element(By.PARTIAL_LINK_TEXT, pn)


@exc_handler
def product_details_click(d, sr):
    ActionChains(d).click(sr).perform()


@exc_handler
def gather_info(d):
    """
    param d: Is for driver
    return: The list of str widgets values, including productname, label,
    discount, price, description
    """
    productname = d.find_element(By.CSS_SELECTOR, """#pdpMain > 
    div.productdetail_bg > div > div.productinfo > h1""")
    label = d.find_element(By.CSS_SELECTOR, """#pdpMain > 
    div.productdetail_bg > div > div.productinfo > div.product_cart_block > 
    div.product_attributes_wrapper.rbk_shadow_angle >
     div.variationattributes > div > div.selectedvarval.swatches_info""")
    discount = d.find_element(By.CSS_SELECTOR, """#pdpMain >
     div.productdetail_bg > div > div.productinfo >
     div.product_cart_block > div.product-tocart.shk-item >
      form > div > div > div > div > div""")
    price = d.find_element(By.CSS_SELECTOR, """#pdpMain > div.productdetail_bg >
     div > div.productinfo > div.product_cart_block >
      div.product-tocart.shk-item > form > div > div > div > div >
       span.salesprice > span""")
    description = d.find_element(By.CSS_SELECTOR, """#pdpMain >
     div.productdetail_bg > div > div.productinfo > div.product_cart_block >
      div.short_description > p""")
    return (productname.text, label.text, discount.text, price.text,
            description.text)


def testing_info(pril):
    tested_object = TestFunctions(pril)
    tested_object.length_check()
    tested_object.content_check()


def main(path, catalog_href, products_limit, product_name):
    driver = driver_options()
    driver.get(path)

    url_composition(driver, catalog_href, products_limit)

    product_info_list = []
    pages_amount = pages_calc(driver, products_limit)
    for page in range(pages_amount):
        search_result = product_search(driver, product_name)
        if search_result:
            product_details_click(driver, search_result)
            product_info_list = gather_info(driver)
            break

    # print(product_info_list)
    testing_info(product_info_list)


if __name__ == '__main__':
    # Initial URL.
    path = f"https://www.adishop.by/"
    # Catalog for men's wears. By.XPATH
    catalog_href = """//*[@id="header"]/div/div[2]/ul[1]/li[2]"""
    # Limit for one-page products amount indication. Possible options 15, 30,
    # 60, 90.
    products_limit = "90"
    # Product name User is going to search
    product_name = "Худи"

    main(path, catalog_href, products_limit, product_name)
