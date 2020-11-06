from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_ICON = (By.ID, 'nav-cart')
EMPTY = (By.CSS_SELECTOR, '.sc-your-amazon-cart-is-empty h2')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
LEGO_HARRY = (By.CSS_SELECTOR, '#anonCarousel1 .a-section .a-size-mini .a-link-normal')
ADD_TO_CART = (By.ID, 'add-to-cart-button')







@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_FIELD)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(1)

@when('Choose a first item in result list')
def click_first_item(context):
    context.driver.find_element(*LEGO_HARRY).click()
    sleep(1)

@then ('Add it to cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(1)






# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
#     assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
#
#
# @then('First result contains {search_word}')
# def verify_first_result(context, search_word):
#     first_result = context.driver.find_element(*RESULTS).text
#     print('\n{}'.format(first_result))
#     assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)