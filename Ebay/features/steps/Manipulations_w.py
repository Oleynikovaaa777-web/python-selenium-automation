from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART = (By.XPATH, '//a[@title="Your shopping cart"]')
SEARCH_INPUT = (By.NAME, '_nkw')
SEARCH_SUBMIT = (By.ID, 'gh-btn')
ADD_TO_CART =(By.ID, 'isCartBtn_btn')
EMPTY_CART = (By.XPATH, '//span[contains(text(), "You don\'t have any items in your cart")]')
IPHONE =


@when('Go to cart')
def_click_cart(context):
cart = context.driver.find_element(*CART)
    cart.click()




@when('Check cart is empty')



@when('Open another window')

@when('Switch to new window')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)





@when('Add to cart')

@when('Close pop window')

@when('Close 1 window')

@when('Switch to window 1')

@when('Refresh window and check now cart includes iPhone')
