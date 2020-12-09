from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.XPATH, '//a[@title="Your shopping cart"]')
SEARCH_INPUT = (By.NAME, '_nkw')
SEARCH_SUBMIT = (By.ID, 'gh-btn')
ADD_TO_CART =(By.ID, 'isCartBtn_btn')
EMPTY_CART = (By.XPATH, '//span[contains(text(), "You don\'t have any items in your cart")]')
SEARCH_RES_ITEM = (By.XPATH, '//ul[contains(@class, "srp-results")]//li[contains(@class, "s-item")][2]//h3')
I_CART = (By.XPATH, '//div[@data-test-id="cart-bucket"]')
POP_WINDOW = (By.XPATH, '//div[@id="ADDON_0"]')
CLOSE_POPUP = (By.XPATH, '//button[contains(text(),"No thanks")]')






@when('Go to cart')
def click_cart(context):
    cart = context.driver.find_element(*CART)
    cart.click()
    sleep(5)

@when('Check cart is empty')
def empty_cart(context):
    e_cart = context.driver.find_element(*EMPTY_CART).text
    assert 'You don\'t have any items in your cart' in e_cart, "Expected word '{}' in message, but got '{}'".format('You don\'t have any items in your cart', e_cart)
    sleep(5)



@when('Save current window')
def current_window(context):
    origin_window = context.driver.current_window_handle
    context.origin_window = origin_window
    sleep(5)



@when('Open another window')
def open_new_window(context):
    context.driver.execute_script("window.open('');")
    sleep(5)


@when('Switch to new window')
def switch_to_new_window(context):
    windows = context.driver.window_handles
    for window in windows:
        if window != context.origin_window:
            context.driver.switch_to.window(window)
            break
        sleep(5)




@when('Choose device')
def choose_device(context):
    iphone = context.driver.find_element(*SEARCH_RES_ITEM)
    iphone.click()
    sleep(3)


@when('Add to cart')
def add_to_cart(context):
    cart = context.driver.find_element(*ADD_TO_CART)
    cart.click()
    sleep(3)

@when('Close pop window')
def pop_window(context):
    popup_window = context.driver.find_elements(*POP_WINDOW)
    if len(popup_window) > 0:
        close_popup = context.driver.find_element(*CLOSE_POPUP)
        close_popup.click()
        sleep(2)


@when('Close window 2 and switch to window 1')
def close_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.origin_window)
    sleep(5)


@when('Refresh window and check now cart includes lamp')
def refresh_page(context):
    context.driver.refresh()
    sleep(3)


@when('Check if cart contains lamp')
def check_cart(context):
    check_i = context.driver.find_elements(*I_CART)
    if len(check_i):
        print('Cart is not empty')
    # assert 'Apple iPhone 8 Plus 64GB Factory Unlocked Smartphone' in check_i





