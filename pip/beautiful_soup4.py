import requests
from bs4 import BeautifulSoup

# Kun.uz dan oxirgi yangilik mavzunsini olish
sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_='news-title')  # yangiliklarning mavzusini ajratib olamiz
# print(news[0].text)  # eng birinchi yangilikni konsolga chiqaramiz


# Barcha so'ngi yangiliklarni chiqaramiz
i = 0
for item in news:
    i += 1
    print(f'{i} - {item.text}')
