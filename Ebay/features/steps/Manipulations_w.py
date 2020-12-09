from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.XPATH, '//a[@title="Your shopping cart"]')
SEARCH_INPUT = (By.NAME, '_nkw')
SEARCH_SUBMIT = (By.ID, 'gh-btn')
ADD_TO_CART =(By.ID, 'isCartBtn_btn')
EMPTY_CART = (By.XPATH, '//span[contains(text(), "You don\'t have any items in your cart")]')
IPHONE = (By.XPATH, '//h3[contains(text(),"Apple iPhone 8 Plus 64GB Factory Unlocked Smartphone")]')
I_CART = (By.XPATH, '//span[contains(text(),"Apple iPhone 8 Plus 64GB Factory Unlocked Smartphone")]')
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
    iphone = context.driver.find_element(*IPHONE)
    iphone.click()


@when('Add to cart')
def add_to_cart(context):
    cart = context.driver.find_element(*ADD_TO_CART)

@when('Close pop window')
def pop_window(context):
    popup_window = context.driver.find_element(*POP_WINDOW)
    if len(popup_window) > 0:
        close_popup = context.driver.find_element(*CLOSE_POPUP).click()


@when('Close window 2 and switch to window 1')
def close_window(context):
    context.driver.close()
    context.driver.switchTo().window(origin_window)
    sleep(5)


@when('Refresh window and check now cart includes iPhone')
def refresh_page(context):
    context.driver.get('https://www.ebay.com/')
    context.driver.refresh()


@when('Check if cart contains iPhone')
def check_cart(context):
    check_i = context.driver.get(*I_CART).text
    assert 'Apple iPhone 8 Plus 64GB Factory Unlocked Smartphone' in check_i





