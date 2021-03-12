import requests
from bs4 import BeautifulSoup
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()
text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='post')
result_list = list()

for article in articles:
    titles = [x.text.strip().lower() for x in article.find_all('a', class_='post__title_link')]
    hubs = [x.text.strip().lower() for x in article.find_all('a', class_='hub-link')]
    posts_text = [x.text.strip().lower() for x in article.find_all('div', class_='post__text')]

    for post in posts_text:
        if any(x in post for x in KEYWORDS):
            title_el = article.find('a', class_='post__title_link')
            title_result = title_el.text
            time_el = article.find('span', class_='post__time')
            href = title_el['href']
            result = f'<{time_el.text}> - <{title_result}> - <{href}>'
            if result not in result_list:
                result_list.append(result)
            break

    for title in titles:
        if any(x in title for x in KEYWORDS):
            title_el = article.find('a', class_='post__title_link')
            title_result = title_el.text
            time_el = article.find('span', class_='post__time')
            href = title_el['href']
            result = f'<{time_el.text}> - <{title_result}> - <{href}>'
            if result not in result_list:
                result_list.append(result)
            break

    for hub in hubs:
        if any(x in hub for x in KEYWORDS):
            title_el = article.find('a', class_='post__title_link')
            title_result = title_el.text
            time_el = article.find('span', class_='post__time')
            href = title_el['href']
            result = f'<{time_el.text}> - <{title_result}> - <{href}>'
            if result not in result_list:
                result_list.append(result)
            break

pprint(result_list)