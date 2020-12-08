
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.NAME, '_nkw')
SEARCH_SUBMIT = (By.ID, 'gh-btn')
FAST_FREE = (By.XPATH, '//span[@class="s-item__fnf"]')
FIRST_RESULT = (By.XPATH, '//li[contains(@class, "s-item")][1]//h3')
ADD_TO_CART = (By.ID, 'isCartBtn_btn')
POP_UP = (By.ID, 'ADDON_0')
CLOSE_POPUP = (By.XPATH, '//div[@id="ADDON_0"]//button[contains(@class, "addon-overlay-close-button")]')
CART_1 = (By.XPATH, '//h1[contains(text(), "Shopping cart (1 item)")]')



# @given('Open Ebay page')
# def open_ebay(context):
#     context.driver.get('https://www.ebay.com/')

# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
# @when('Search for {search_word}')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(5)


# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(5)

@when('Count items with label Fast/n free')
def count_items(context):
    count_fast_free = context.driver.find_elements(*FAST_FREE)
    print(len(count_fast_free))
    sleep(5)



@when('Open first item result')
def first_result(context):
    open_first_res = context.driver.find_element(*FIRST_RESULT)
    open_first_res.click()

@when('Add item to cart')
def add_to_cart(context):
    add_item = context.driver.find_element(*ADD_TO_CART)
    add_item.click()

@when('If have popup close it')
def pop_up(context):
    pop_up_w = context.driver.find_elements(*POP_UP)
    if len(pop_up_w) > 0:
        close_window = context.driver.find_element(*CLOSE_POPUP)
        close_window.click()





@then('Check 1 item in cart')
def cart_contains_1(context):
    cart_1 = context.driver.find_element(*CART_1).text
    assert 'Shopping cart (1 item)' in cart_1

