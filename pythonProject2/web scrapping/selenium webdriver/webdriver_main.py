from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" ,True)

driver =webdriver.Chrome(options = chrome_options)
# driver.get("https://www.amazon.com")
#
# driver.find_element(By.CLASS_NAME , value= "a-price-whole")

# driver.close()

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR ,".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR ,".event-widget li a")
events = {f"{i}.(time : {event_times[i].text},name : {event_names[i].text})" for i in range(0, len(event_times))}

print(events)




driver.quit()
