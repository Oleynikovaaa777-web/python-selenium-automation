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

add_to_cart = driver.find_element(By.XPATH,"//input[@id='add-to-cart-button']")
add_to_cart.click()

# To remove notification:

# continue_button = driver.find_element(By.XPATH, "//span[@id='a-autoid-20-announce']")
# continue_button.click()

# cancel_button = driver.find_element(By.XPATH, "//button[@aria-label='Close']")
# cancel_button.click()

# no_thanks = driver.find_element(By.XPATH, "//span[@id='a-autoid-21-announce']")
# no_thanks.click()

#
# cart_subtotal = driver.find_element(By.XPATH,  "//div[h1]")
#
#
#
#
#
#
#
#
# assert 'Added to Cart' in cart_subtotal.text, \
#     f'Expected \Your Shopping Cart is empty, but got {cart_subtotal.text}'




driver.quit()
