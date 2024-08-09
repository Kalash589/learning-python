from bs4 import BeautifulSoup
#import lxml

with open(file = "website.html") as file:
    content = file.read()

soup = BeautifulSoup(content , "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

anchor_tags = soup.find_all(name="a")
print(anchor_tags)

section_heading = soup.find(name="h3" , class_="heading")

heading = soup.find(name="h1" , id="name")
print(section_heading.get_text())
print(section_heading.get("class"))
print(Ssection_heading)

#select for css selector  
soup.select()
soup.select_one()

