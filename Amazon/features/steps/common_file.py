#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
#
# @when ('Input {search_word} into search field')
# def input_search_word(context, search_word):
#         search = context.driver.find_element(*SEARCH_FIELD)
#         search.clear()
#         search.send_keys(search_word)
#         sleep(4)
#
#
#
# @when ('Click on search button')
# def click_search(context):
#     search_button = context.driver.find_element(*SEARCH_BUTTON)
#     search_button.click()
#     sleep(4)