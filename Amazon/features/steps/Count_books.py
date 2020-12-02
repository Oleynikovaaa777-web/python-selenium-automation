# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
# FANTASY_BOOK = (By.CSS_SELECTOR, 'span.celwidget div.a-section.aok-relative.s-image-fixed-height')
# ALL_PRICES = (By.XPATH,
#               "//div[@data-component-type='s-search-result']//div[contains(@class, 'a-spacing-top-small')]//span[contains(@class, 'a-price-whole')]")
#
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_FIELD)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     click_icon = context.driver.find_element(*SEARCH_BUTTON)
#     click_icon.click()
#     sleep(6)
#
#
# @when('Find all prices')
# def observe_all_prices(context):
#     all_prices = context.driver.find_elements(*ALL_PRICES)
#     print(len(all_prices))
#
#
# @then('Count how many books expensive then 20$')
# def count_books(context):
#     all_prices = context.driver.find_elements(*ALL_PRICES)
#     count = 0
#     for x in all_prices:
#         y = (int(x.text))
#         if y > 20:
#             count += 1
#             print(y)
#     print(count)
