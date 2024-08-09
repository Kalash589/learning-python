import requests
from bs4 import BeautifulSoup

response =requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page =response.text

soup = BeautifulSoup(yc_web_page , "html.parser")
articles = soup.find_all(name="a" , class_="storylink")
article_text=[]
article_link =[]

for article in articles:
    text = article.get_text()
    article_text.append(text)
    link = article.get("href")
    article_link.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span" , class_="score")]

highest = max(article_upvotes)
high_index = article_upvotes.index(highest)
print(article_link[high_index])
print(article_text[high_index]) 
print(highest )
# article_link = article_tag.get("href")
# article_text = article_tag.get_text()
# print(article_text)
# print(article_link)

# print(article_upvotes)
#

