# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
#
# CART_ICON = (By.ID, 'nav-cart')
# EMPTY = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty h2')
# SEARCH = (By.ID, 'twotabsearchtextbox')
# SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
# LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
# ADD_TO_CART = (By.ID, 'add-to-cart-button')
# CART_COUNTER = (By.ID, 'nav-cart-count')
#
#
#
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
#
# @when('Click on Cart icon')
# def click_cart_icon(context):
#     context.driver.find_element(*CART_ICON).click()
#     sleep(1)
#
#
#
#
# @then('Verify that Cart is empty')
# def cart_is_empty(context):
#     result_empty = context.driver.find_element(*EMPTY).text
#     print('\n{}'.format(result_empty))
#     assert 'empty' in result_empty, "Expected word '{}' in message, but got '{}'".format('empty', result_empty)