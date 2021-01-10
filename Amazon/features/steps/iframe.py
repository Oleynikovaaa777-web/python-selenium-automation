from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


CART = (By.XPATH, '//div[@class="MyCart__icon"]')
EMPTY_CART = (By.CSS_SELECTOR, '.empty-cart__message.empty-cart__message--primary')
SEARCH_F = (By.ID, 'headerSearch')
SUBMIT_BUTTON = (By.ID, 'headerSearchButton')
FIRST_ITEM = (By.XPATH, '//div[@class="results-wrapped"]//div[contains(@class, "browse-search__pod")][1]//a[@class="product-pod--ie-fix"]')
ADD_TO_CART = (By.XPATH, '//button[@class="bttn bttn--primary"]')
POPUP = (By.XPATH, '//iframe[@class="thd-overlay-frame"]')
CLOSE_POPUP = (By.CSS_SELECTOR, '.thd-overlay__close')
CART_NOT_EMPTY = (By.CSS_SELECTOR, '.MyCart__contents')
PICKIT_UP = (By.XPATH, '//button[@data-automation-id="indexYesIwillPickupHereButton"]')






@given('Open home depot page')
def open_homedepot(context):
    context.driver.get('https://www.homedepot.com/')



@when('Go to cart')
def go_to_cart(context):
    cart = context.driver.find_element(*CART)
    cart.click()
    sleep(3)




@when('Check cart is empty')
def empty_cart(context):
    empty = context.driver.find_element(*EMPTY_CART).text
    assert 'There\'s Nothing Here Yet' in empty
    sleep(3)



@when('Open new window')
def open_new_window(context):
    context.driver.execute_script("window.open('');")
    sleep(3)




@when('Switch to new window')
def switch_to_new_window(context):
    context.origin_window = context.driver.current_window_handle
    windows = context.driver.window_handles
    for window in windows:
        if window != context.origin_window:
            context.driver.switch_to.window(window)
            break




@when('Open home depot page')
def open_homedepo_page(context):
    context.driver.get('https://www.homedepot.com/')





@when('Search for {search_word}')
def input_search_word(context, search_word):
    search = context.driver.find_element(*SEARCH_F)
    search.clear()
    search.send_keys(search_word)
    search_submit = context.driver.find_element(*SUBMIT_BUTTON)
    search_submit.click()
    sleep(4)




@when('Choose first item')
def first_item(context):
    first = context.driver.find_element(*FIRST_ITEM)
    first.click()
    sleep(3)




@when('Add to cart')
def add_to_cart(context):
    add_cart = context.driver.find_element(*ADD_TO_CART)
    add_cart.click()
    sleep(3)




@when('Close popup window')
def close_popup(context):
    iframe = context.driver.find_element(*POPUP)
    context.driver.switch_to.frame(iframe)
    ipickit_up = context.driver.find_element(*PICKIT_UP)
    ipickit_up.click()
    context.driver.switch_to.default_content()
    sleep(4)


@when('Close new window and switch on previous one')
def close_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.origin_window)
    print(context.driver.current_window_handle)
    sleep(2)

#

#
@when('Refresh page')
def refresh_page(context):
    context.driver.refresh()




@then('Check cart now is not empty')
def not_empty_cart(context):
    not_empty = context.driver.find_element(*CART_NOT_EMPTY).text
    assert '1 item' in not_empty





