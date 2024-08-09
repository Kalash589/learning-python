from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach" , True)


driver = webdriver.Chrome(options=chrome_option)

driver.get("https://tinder.com/")

sleep(10)

log_in = driver.find_element(By.XPATH,value='//*[text()="Log in"]' )
log_in.click()






























# driver.quit()