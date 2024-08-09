import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
file = response.text

soup = BeautifulSoup(file , "html.parser")
movie_tags = soup.find_all(name="h3" , class_="title")
names = []
for movie_tag in movie_tags:
    text = movie_tag.get_text()
    names.append(text)

movie_names = names[::-1]
print(movie_names)

i=0
with open("100_movies.txt" , "w") as file:
    for i in range(len(movie_names) - 1):
        file.write(f"{movie_names[i]}\n")
