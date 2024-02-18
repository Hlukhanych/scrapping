from requests import get
from bs4 import BeautifulSoup
import sys

# 2

url = "https://lpnu.ua/lvivska-politekhnika/kerivnytstvo-universytetu"
page = get(url)

# print(page.text)

# 3

soup = BeautifulSoup(page.content, 'html.parser')
soup_class = soup.find(class_="field field--name-field-alternative-body field--type-entity-reference-revisions field--label-hidden field--items")

for a in soup_class.find_all(class_="field field--name-field-person-name field--type-link field--label-hidden field--item"):
    a = a.find('a')
    name = a.find(string=True, recursive=False)
    link = a.get('href')
    # print(f"{name} - {'https://lpnu.ua' + link}")

# 4

for a in soup_class.find_all(class_="field field--name-field-person-name field--type-link field--label-hidden field--item"):
    a = a.find('a')
    name = a.find(string=True, recursive=False)
    link = a.get('href')
    link_url = 'https://lpnu.ua' + link
    print(f"{name} - {link_url}: ")


    try:
        link_page = get(link_url)
        link_soup = BeautifulSoup(link_page.content, 'html.parser')
        link_soup_class = link_soup.find(class_="field--item")

        for l in link_soup_class.find_all("a"):
            name_l = l.find(string=True, recursive=False)
            link_l = l.get('href')

            print(f"{name_l} - {link_l}")

    except:
        print("error")

# 5

question = input("write to file? (y/n): ")

if question == "y":
    file = "un.txt"

    with open(file, "w", encoding="utf-8") as file:
        print("wait...")
        for a in soup_class.find_all(
                class_="field field--name-field-person-name field--type-link field--label-hidden field--item"):
            a = a.find('a')
            name = a.find(string=True, recursive=False)
            link = a.get('href')
            link_url = 'https://lpnu.ua' + link
            file.write(f"{name} - {link_url}: \n")

            try:
                link_page = get(link_url)
                link_soup = BeautifulSoup(link_page.content, 'html.parser')
                link_soup_class = link_soup.find(class_="field--item")

                for l in link_soup_class.find_all("a"):
                    name_l = l.find(string=True, recursive=False)
                    link_l = l.get('href')

                    file.write(f"{name_l} - {link_l} \n")

            except:
                file.write("error \n")

else:
    print("end")