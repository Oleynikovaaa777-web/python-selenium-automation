# Ex.4

# Create your own test case to add any product you want into the cart, and make sure it’s
# there (check for the number of items in the cart OR open the cart and verify it’s there,
# up to you!)
# * - Not Required


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com//')

best_sellers = driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
best_sellers.click()

product = driver.find_element(By.XPATH,"//img[@alt='Echo Dot (3rd Gen) - Smart speaker with Alexa - Charcoal']")
product.click()

add_to_cart =



#
# cart = driver.find_element(By.XPATH,"//a[@id='nav-cart']")
# cart.click()


# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Dress')
#
# # wait for 4 sec
# sleep(4)



# empty_cart= driver.find_element(By.XPATH,"//div[h2]")





# assert 'Your Shopping Cart is empty' in empty_cart.text, \
#     f'Expected \Your Shopping Cart is empty', but got {empty_cart.text}'




driver.quit()
