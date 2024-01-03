import requests
from bs4 import BeautifulSoup


url = "https://sputnik.by/geoBelarus/"
req = requests.get(url)
src = req.text

soup = BeautifulSoup(src, 'html.parser')
all_news_hrefs = soup.find_all(class_="list__title")

all_news_dict = {} #Словарь в котором хранится заголовок статьи и ссылка на неё
for item in all_news_hrefs:
    item_text = item.text
    item_href = "https://sputnik.by/geoBelarus" + item.get("href")
    all_news_dict[item_text] = item_href #Запись значений в словарь
    print(f"{item_text}: {item_href}")

search_word = input("Введите слово: ")
#search_word  = 'оценил' #Ключевое слово
result = [(key, value) for key, value in all_news_dict.items() if search_word in key]

# Выводим результат
print(f'По ключевому слову надено {len(result)} новость(-ей), содержащих слово "{search_word}":')
for key, value in result:
    print(f'{key}: {value}')