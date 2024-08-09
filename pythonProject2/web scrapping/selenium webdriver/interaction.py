from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com")

fname_filler = driver.find_element(By.XPATH , value="/html/body/form/input[1]")
fname_filler.send_keys("kalash")

lname_filler = driver.find_element(By.XPATH , value="/html/body/form/input[2]")
lname_filler.send_keys("gawande")

email_filler = driver.find_element(By.XPATH , value="/html/body/form/input[3]")
email_filler.send_keys("kalashgawande")

button = driver.find_element(By.XPATH , value="/html/body/form/button")
# button.send_keys(Keys.ENTER)

#count.click()
#By.LINK_TEXT , value""
#search.send_keys("text...")
#Keys.ENTER






# driver.quit()
