from behave import given, when, then
from time import sleep


# @when('Save current window')
# def current_window(context):
#     origin_window = context.driver.current_window_handle
#     context.origin_window = origin_window
#
#
#
# @when('Open new window')
# def open_new_window(context):
#     context.driver.execute_script("window.open('');")
#
#
# @when('Switch to new window')
# def switch_to_new_window(context):
#     windows = context.driver.window_handles
#     for window in windows:
#         if window != context.origin_window:
#             context.driver.switch_to.window(window)
#             break



@when('Make some manipulations')
def make_some_manipulations(context):
    context.driver.get('https://www.ebay.com')
    print(context.driver.current_window_handle)
    sleep(4)


@then('Switch to origin window')
def switch_to_origin_window(context):
    context.driver.switch_to.window(context.origin_window)
    print(context.driver.current_window_handle)