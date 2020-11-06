#
# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
#
# SEARCH_INPUT = (By.NAME, '_nkw')
# SEARCH_SUBMIT = (By.ID, 'gh-btn')
# RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[@class='srp-river-results clearfix']")
# RESULTS = (By.XPATH, "//h3[@class='s-item__title']")


# @given('Open Ebay page')
# def open_ebay(context):
#     context.driver.get('https://www.ebay.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)
#
#
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