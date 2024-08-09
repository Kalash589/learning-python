import dotenv
import requests
from bs4 import BeautifulSoup
import smtplib
import pytest_dotenv



header ={
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding" : "gzip, deflate, br" ,
    "Accept-Language" : "en-IN,en-GB;q=0.9,en;q=0.8" ,
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15"
}


my_email = "kalashig333@gmail.com"
password = "vktb qbcy acjy vuzc"
smtp_adress = "smtp.gmail.com"

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1" ,headers=header )
html_file = response.text

soup = BeautifulSoup(html_file , "html.parser")
# print(soup.prettify())
price_tag = soup.find(name="span" , class_="aok-offscreen").get_text().split("$")[1]
price_float = float(price_tag)


product_name = soup.find(name="span" , id="productTitle").get_text().strip()
print(product_name)

buy_price = 100

product_link = "https://appbrewery.github.io/instant_pot/"
if price_float <= buy_price :
    connection = smtplib.SMTP(smtp_adress, port=587)
    connection.starttls()
    connection.login(user=my_email , password=password)
    connection.sendmail(from_addr=my_email , to_addrs=my_email , msg=f"subject:Amazon Price Alert \n\n {product_name} is on sale for : ${price_float} \nhere is the link to buy {product_link}".encode('utf-8'))
    connection.close()
else:pass

