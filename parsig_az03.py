import requests
from bs4 import BeautifulSoup
import time
import random
import csv
from datetime import datetime

# URL страницы
url = "https://www.divan.ru/tomsk/category/divany-i-kresla"

# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://www.divan.ru/'
}

try:
    # Выполняем запрос с задержкой и случайным юзер-агентом
    time.sleep(random.uniform(1.0, 3.0))  # Случайная задержка между запросами

    response = requests.get(url, headers=headers, timeout=10)
    response.encoding = 'utf-8'  # Устанавливаем кодировку

    print(f"Статус код: {response.status_code}")

    if response.status_code == 200:
        # Создаем объект BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем все блоки с товарами
        products = soup.find_all('div', class_='lsooF')

        if not products:
            print("Не найдено ни одного товара. Возможно, изменилась структура страницы.")
            exit()

        print(f"Найдено товаров: {len(products)}")

        # Создаем CSV файл для сохранения результатов
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'divan_prices_{timestamp}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Название', 'Цена', 'Ссылка']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Проходим по всем найденным товарам
            for product in products:
                # Извлекаем название товара
                name_tag = product.find('span', itemprop='name')
                name = name_tag.text.strip() if name_tag else "Название не указано"

                # Извлекаем цену
                price_tag = product.find('meta', itemprop='price')
                price = price_tag['content'] if price_tag and price_tag.has_attr('content') else "Цена не указана"

                # Извлекаем ссылку на товар
                link_tag = product.find('a', class_='_1mUsk')
                link = "https://www.divan.ru" + link_tag['href'] if link_tag else "Ссылка не найдена"

                # Выводим информацию в консоль
                print(f"Товар: {name}")
                print(f"Цена: {price} руб.")
                print(f"Ссылка: {link}")
                print("-" * 50)

                # Записываем в CSV
                writer.writerow({
                    'Название': name,
                    'Цена': price,
                    'Ссылка': link
                })

        print(f"\nДанные успешно сохранены в файл: {filename}")
    else:
        print(f"Ошибка запроса: {response.status_code}")

except requests.exceptions.Timeout:
    print("Ошибка: Время ожидания истекло. Сайт недоступен.")
except requests.exceptions.RequestException as e:
    print(f"Ошибка подключения: {str(e)}")
except Exception as e:
    print(f"Неизвестная ошибка: {str(e)}")
