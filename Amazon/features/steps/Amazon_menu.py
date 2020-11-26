# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# MENU = (By.ID,'nav-hamburger-menu')
#
# ITEMS = (By.XPATH,"//div[@id='hmenu-content']//ul[contains(@class, 'hmenu-visible')]//div[contains(@class, 'hmenu-item')][contains(@class, 'hmenu-title')]")
#
#
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
#
# @when('Click on menu')
# def click_menu(context):
#     context.driver.find_element(*MENU).click()
#     sleep(4)
#
# @then('Get all items')
# def get_items(context):
#     all_items = context.driver.find_elements(*ITEMS)
#     print(len(all_items))


