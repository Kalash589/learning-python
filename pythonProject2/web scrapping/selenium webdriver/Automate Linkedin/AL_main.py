import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USERNAME = "kalashig333@gmail.com"
PASSWORD = "kalashanshu786"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/home")

sign_in = driver.find_element(By.XPATH,"/html/body/nav/div/a[2]")
sign_in.click()

username = driver.find_element(By.XPATH , value='//*[@id="username"]')
username.send_keys("kalashig333@gmail.com")

password = driver.find_element(By.XPATH , value='//*[@id="password"]')
password.send_keys("kalashanshu786")

signing = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')
signing.click()

search = driver.find_element(By.XPATH , value='//*[@id="global-nav-typeahead"]/input')
print(search)
search.click()
search.send_keys("python developer")
search.send_keys(Keys.ENTER)

# first_option = driver.find_element(By.CSS_SELECTOR , 'role="list" and [contains(@class , "reusable-search__result-container")]')
# print(first_option)

ul_role = driver.find_element(By.CLASS_NAME, "scaffold-layout__main")
# print(ul_role)
fo = ul_role.find_element(By.CLASS_NAME , "reusable-search__result-container")
fo.click()



# easy_apply = driver.find_element(By.XPATH , value='//*[@id="ember920"]')
# easy_apply.click()
#
# mobile_number = driver.find_element(By.XPATH , value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3960096036-2817740914-phoneNumber-nationalNumber"]')
# mobile_number.send_keys("9527002008")
#
# next = driver.find_element(By.XPATH , value='//*[@id="ember1020"]')
# next.click()
#
# # upload_resume = driver.find_element(By.XPATH , value='//*[@id="ember1009"]/div/div[2]/form/div/div/div/div[2]/div/label/span')
# # upload_resume.click()
#
# next2 = driver.find_element(By.XPATH , value='//*[@id="ember1020"]/span')
# next2.click()
#


