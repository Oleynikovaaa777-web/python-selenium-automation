# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
# SEARCH_BUTTON = (By.ID, 'nav-search-submit-text')
# FANTASY_BOOK = (By.CSS_SELECTOR, 'span.celwidget div.a-section.aok-relative.s-image-fixed-height')
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_FIELD)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
# @when('Search for fantasy book')
# def search_fantasy_book(context):
#     context.driver.find.element(*SEARCH_FIELD)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_BUTTON).click()
#     sleep(6)
#
#
#
# @then('On result page should be {count_of_books} results')
# def count_books(context, count_of_books):
#         fantasy_books = context.driver.find_elements(*FANTASY_BOOK)
#         print(len(fantasy_books))
#         print(int(count_of_books))
#         assert len(fantasy_books) == int(count_of_books)






