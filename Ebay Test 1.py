from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.ebay.com/')


login = driver.find_element(By.XPATH,'//span[@id="gh-ug"]//a[text()="Sign in"]')




login.click()



# # wait for 4 sec
# sleep(4)
#
#
#
# driver.quit()
