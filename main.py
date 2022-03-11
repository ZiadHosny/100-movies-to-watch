import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

movies = [film.get_text() for film in soup.find_all(name ='h3', class_ ='title')]
all =movies[::-1]
with open('file.txt' , 'w') as file:
    for movie in all:
        file.write(f'{movie}\n')
    

