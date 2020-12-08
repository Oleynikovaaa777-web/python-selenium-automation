from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from random import choice

CART_ICON = (By.ID, 'nav-cart')
EMPTY = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty h2')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
FIRST_ELEMENT = (By.XPATH, "//div[contains(@class, 's-result-list')][2]/div[contains(@class, 's-result-item')][3]//h2/a")
ADD_TO_CART = (By.ID, 'add-to-cart-button')
ADDED_TO_CART_ELEMENT = (By.CSS_SELECTOR, '.sc-product-title')
DELETE_ITEM = (By.XPATH, '//input[@data-action="delete"]')








@when('Choose a first item in result list')
def click_first_item(context):
    first_item = context.driver.find_element(*FIRST_ELEMENT)
    first_item.click()
    sleep(4)


# @when ('Add it to cart')
# def add_to_cart(context):
#     add_it_to_cart = context.driver.find_element(*ADD_TO_CART)
#     results = [True, False]
#     if choice(results):
#         add_it_to_cart.click()
#     sleep(4)


# @when ('Click to Cart icon')
# def cart_icon(context):
#     cart = context.driver.find_element(*CART_ICON)
#     cart.click()
#     sleep(3)



@when ('If cart is not empty - delete item and check cart is empty')
def check_cart_is_empty(context):
    added_element = context.driver.find_elements(*ADDED_TO_CART_ELEMENT)
    if len(added_element) > 0:
        delete = context.driver.find_element(*DELETE_ITEM)
        delete.click()



# @then ('Check cart is empty')
# def check_is_not_empty(context):
#     empty_element = context.driver.find_element(*EMPTY)
#     assert 'Your Amazon Cart is empty' in empty_element.text, \
#         f'Expected Your Amazon Cart is empty, but got {empty_element.text}'
