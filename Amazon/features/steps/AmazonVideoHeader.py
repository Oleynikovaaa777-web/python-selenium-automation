# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# PRIME_VIDEO_LINK = (By.CSS_SELECTOR, '#nav-xshop a[data-csa-c-content-id="nav_cs_bestsellers"]')
# HOME_VIDEO_LINK = (By.CSS_SELECTOR, '#zg_tabs ul li:first-child')
#
# @when('Click to Prime Video Header Link')
# def click_prime_video(context):
#     prime_video = context.driver.find_element(*PRIME_VIDEO_LINK)
#     prime_video.click()
#     sleep(2)
#
# @then('Home video link has active class')
# def check_active_class(context):
#     home_link = context.driver.find_element(*HOME_VIDEO_LINK)
#     home_link_classes = home_link.get_attribute("class")
#     assert 'zg_selected' in home_link_classes