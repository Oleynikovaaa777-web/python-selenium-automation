# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# READ_MORE = (By.XPATH, "//body/div[@id='mainContent']/div[@id='rtm_list2']/div[2]/div[1]/a[1]/div[2]")
#
# COVID_TITLE = (By.XPATH, "//h1[@class='c-hero-2__title']")
#
# EBAY_TITLE = (By.XPATH, "//a[@title='My eBay']")
#
#
# @given('Open Ebay page')
# def open_ebay(context):
#     context.driver.get('https://www.ebay.com/')
#
#
# @when('Click on about COVID-19')
# def click_read_more(context):
#     read_more_ = context.driver.find_element(*READ_MORE)
#     read_more_.click()
#     sleep(4)
#
#
# @when('Check if COVID-19 contains in title')
# def check_title(context):
#     title_1 = context.driver.find_element(*COVID_TITLE).text
#     print(title_1)
#     assert 'COVID-19' in title_1
#         # , "Expected word '{}' in message, but got '{}'".format('COVID-19', )
#     sleep(4)
#
#
# @when('Go back')
# def go_back(context):
#     context.driver.back()
#     sleep(4)
#
#
# @when('Check current page is {expected_current_url} page')
# def check_url(context, expected_current_url):
#     current_url = context.driver.current_url
#     print(current_url)
#     assert expected_current_url.lower() in current_url.lower(), f'Expected {expected_current_url} be in {current_url}, but it\'s not there'
#
#
# @then('Check if title contains text eBay')
# def title(context):
#     title_ebay = context.driver.find_element(*EBAY_TITLE).text
#     assert 'eBay' in title_ebay
#     sleep(4)
#
