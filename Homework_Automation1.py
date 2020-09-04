
# XPath=”//tagname[@attribute='value']”
#

#
#
# 1.
# Amazon
# logo
#
# $x("//i[@class='a-icon a-icon-logo']")
#
# 2.
# Sign in
# $x("//i[@class='a-icon a-icon-logo']")
#
# 3.
# Continue
# button
#
# $x("//input[@id='continue']")
#
# 4.
# Need
# help
# link
# $x("//span[@class='a-expander-prompt']")
#
# 5.
#
# Forgot
# your
# password
#
#
#
#
# $x("//a[@id='auth-fpp-link-bottom']")
#
# 6.
# Other
# issues
# with Sign - In link
#
# $x("//a[@id='ap-other-signin-issues-link']")
#
#
#
#
# 7.
# Create
# your
# Amazon
# account
# button
#
#
# $x("//a[@id='createAccountSubmit']")
#
#
#
#
# 8.
# Conditions
# of
# use
# link
#
#
# $x("//*[text()='Conditions of Use']")
#
# 9.
# Privacy
# Notice
# link
#
#
#
# $x("//*[text()='Privacy Notice']")





from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com//')



Help = driver.find_element(By.XPATH, "//*[text()='Help']")
Help.click()
search = driver.find_element(By.XPATH, "//input[@type='search']")
search.clear()
search.send_keys('Cancel order')
search.click()

sleep(5)





# Go to amazon
#
#
# Help_button=$x("//*[text()='Help']")
#
# Help_button.click()
#
# Search = $x("//input[@type='search']")
#
# search.send_keys('Cancel order')
#
# Click



driver.quit()