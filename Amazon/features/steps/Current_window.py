from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# ALL_ELEM = (By.XPATH'//div[@id = "nav-xshop"]/a')
#
#
#  ‘//a[contains(@href, ‘ ’)]’

# 1  href="/gift-cards/b/?ie=UTF8&amp;node=2238192011&amp
#
# 2 href="/gp/bestsellers/?ref_=nav_cs_bestsellers"
#
# 3 href="/prime?ref_=nav_cs_primelink_nonmember"
#
# 4 href="/gp/help/customer/display.html?nodeId=508510&amp;ref_=nav_cs_customerservice"
#
# 5 href="/gp/new-releases/?ref_=nav_cs_newreleases"
#
# 6 href="/gcx/Gifts-for-Everyone/gfhz/?ref_=nav_cs_giftfinder"
#
# 7 href="/alm/storefront?almBrandId=VUZHIFdob2xlIEZvb2Rz&amp;ref_=nav_cs_whole_foods_in_region"
#
# 8 href="/books-used-books-textbooks/b/?ie=UTF8&amp;node=283155&amp;ref_=nav_cs_books"
#
# 9 href="/stores/node/2528919011/?field-lbr_brands_browse-bin=AmazonBasics&amp;ref_=nav_cs_amazonbasics"
#
# 10 href="/Kindle-eBooks/b/?ie=UTF8&amp;node=154606011&amp;ref_=nav_cs_kindle_books"
#
# 11 href="/toys/b/?ie=UTF8&amp;node=165793011&amp;ref_=nav_cs_toys"
#
# 12 href="/amazon-fashion/b/?ie=UTF8&amp;node=7141123011&amp;ref_=nav_cs_fashion"
#
# 13 href="/b/?_encoding=UTF8&amp;ld=AZUSSOA-sell&amp;node=12766669011&amp;ref_=nav_cs_sell"










GIFT_CARDS = (By.XPATH, '//a[@data-csa-c-slot-id="nav_cs_0"]')

BEST_SELLERS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_bestsellers"]')

PRIME = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_primelink_nonmember"]')

CUSTOMER_SERVICE = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_customerservice"]')

NEW_RELEASES = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_newreleases"]')

FIND_A_GIFT = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_giftfinder"]')

WHOLE_FOODS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_whole_foods_in_region"]')

BOOKS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_books"]')

AMAZONBASICS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_amazonbasics"]')

KINDLE_BOOKS = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_kindle_books"]')

TOYS_GAMES = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_toys"]')

FASHION = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_fashion"]')

SELL = (By.XPATH, '//a[@data-csa-c-content-id="nav_cs_sell"]')

NAV_ELEM = (By.XPATH, '//div[@id = "nav-xshop"]/a')


@then('Can show current window')
def current_window(context):
    # print(context.driver.current_window_handle)
    # context.driver.execute_script("window.open('');")
    elems = context.driver.find_elements(*NAV_ELEM)
    links = [elem for elem in elems]
    print(links)

    for link in elems:
        link.send_keys(Keys.COMMAND + Keys.ENTER)  # open link in new tab keyboard shortcut
        sleep(2)
        context.driver.switch_to_window(context.driver.window_handles[1])  # assuming new tab is at index 1
        context.driver.close()  # closes new tab
        context.driver.switch_to_window(context.driver.window_handles[0])
        sleep(3)




    # for elem in links:
    #     # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
    #     # context.driver.find_element(elem).send_keys(Keys.CONTROL + 't')
    #     # sleep(3)
    #     action = ActionChains(context.driver)
    #     action.key_down(Keys.CONTROL).click(elem).key_up(Keys.CONTROL).perform()
    #     sleep(3)








##########################
    #
    # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
    #
    # context.driver.find_element_by_xpath('//a[@data-csa-c-slot-id="nav_cs_0"]').send_keys(Keys.CONTROL + 't')
    #
    #
    #     windows = context.driver.window_handles
    # sleep(4)
    #
    # print(windows)
    #
    # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('w').key_up(Keys.COMMAND).perform()
    # context.driver.find_element_by_xpath('//a[@data-csa-c-slot-id="nav_cs_0"]').send_keys(Keys.CONTROL + 'w')
    #
    # sleep(3)
#######################################


    #
    #
    # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
    #
    # context.driver.find_element_by_xpath('//a[@data-csa-c-content-id="nav_cs_bestsellers"]').send_keys(Keys.CONTROL + 't')
    #
    # sleep(5)
    #
    # ActionChains(context.driver).key_down(Keys.COMMAND).send_keys('w').key_up(Keys.COMMAND).perform()
    # context.driver.find_element_by_xpath('//a[@data-csa-c-content-id="nav_cs_bestsellers"]').send_keys(Keys.CONTROL + 'w')
    #
    # sleep(3)


#################################










