# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL сайта
url = "https://www.divan.ru/category/divany"

# Выполнение запроса к сайту
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

# Списки для хранения данных
    sofa_names = []
    sofa_prices = []

# Поиск карточек с товарами и извлечение данных
    products = soup.find_all("div", class_="_Ud0k U4KZV")  # Класс div может быть другим на divan.ru

    for product in products:
        # Название дивана
        name = product.find("a", class_="ui-GPFV8 qUioe ProductName ActiveProduct").text.strip()

        # Цена дивана
        price_text = product.find("span", class_="ui-LD-ZU KIkOH").text.strip()
        price = int("".join(filter(str.isdigit, price_text)))  # Преобразуем цену к числу

        sofa_names.append(name)
        sofa_prices.append(price)

# Создание DataFrame и сохранение в CSV
    df = pd.DataFrame({
        "Name": sofa_names,
        "Price": sofa_prices
    })
    df.to_csv("sofa_prices.csv", index=False)

# Вычисление средней цены
    mean_price = df["Price"].mean()
    print(f"Средняя цена на диваны: {mean_price:.2f} руб.")

# Построение гистограммы цен
    plt.figure(figsize=(10, 6))
    plt.hist(df["Price"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Гистограмма цен на диваны")
    plt.xlabel("Цена, руб.")
    plt.ylabel("Частота")
    plt.show()
else:
    print("Не удалось получить данные с сайта.")
