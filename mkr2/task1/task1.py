import requests
from bs4 import BeautifulSoup
import csv

def parse_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = []

    fields = soup.find_all('a', class_='css-z3gu2d')[:50]
    for field in fields:
        field_url = 'https://www.olx.ua/' + field['href']
        field_response = requests.get(field_url)
        field_soup = BeautifulSoup(field_response.text, 'html.parser')

        title = field_soup.find('h4', class_='css-1juynto').text.strip()
        price = field_soup.find('h3', class_='css-12vqlj3').text.strip()
        location = field_soup.find_all('p', class_='er34gjf0')[1].text.strip()
        date = field_soup.find('span', class_='css-19yf5ek').text.strip()

        items.append({
            'Title': title,
            'Price': price,
            'Location': location,
            'Date': date
        })

    return items

def save_to_csv(data, filename='output.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Price', 'Location', 'Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

# url = 'https://www.olx.ua/uk/elektronika/tehnika-dlya-kuhni/plity-pechi/q-духова-шафа/'
# data = parse_data(url)
# save_to_csv(data, 'duhova-shafa.csv')

data = []
for i in range(6):
    print(f'Парсинг з {i} сторінки')
    if i == 0:
        continue
    url = f'https://www.olx.ua/uk/elektronika/tehnika-dlya-kuhni/plity-pechi/q-духова-шафа/?currency=UAH&page={i}'
    data += parse_data(url)
save_to_csv(data, 'duhova-shafa-5.csv')
