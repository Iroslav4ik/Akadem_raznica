import csv
import random
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read(50000)
    return chardet.detect(raw_data)['encoding']


def count_long_titles():
    encoding = detect_encoding('books-en.csv')
    with open('books-en.csv', encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=';')
        count = sum(1 for row in reader if len(row['Book-Title']) > 30)

    with open('long_titles_count.txt', 'w') as f:
        f.write(str(count))


def search_by_author():
    encoding = detect_encoding('books-en.csv')
    author = input("Введите фамилию автора: ")
    results = []

    with open('books-en.csv', encoding=encoding) as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if author.lower() in row['Book-Author'].lower():
                try:
                    price_str = row['Price'].replace(',', '.').strip()
                    if price_str and price_str != '0':
                        price = float(price_str)
                        if price <= 200:
                            results.append(f"{row['Book-Author']} - {row['Book-Title']} ({price:.2f} руб)")
                except (ValueError, TypeError):
                    continue

    with open('books_by_author.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(results) if results else "Книги не найдены")


def generate_bibliography():
    encoding = detect_encoding('books-en.csv')
    with open('books-en.csv', encoding=encoding) as f:
        books = list(csv.DictReader(f, delimiter=';'))

    selected = random.sample(books, min(20, len(books)))
    references = []
    for i, row in enumerate(selected, 1):
        author = row.get('Book-Author', 'Неизвестный автор')
        title = row.get('Book-Title', 'Без названия')
        year = row.get('Year-of-Publication', 'нет данных')
        references.append(f"{i}. {author}. {title} - {year}")

    with open('bibliography.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(references))


if __name__ == "__main__":
    count_long_titles()
    search_by_author()
    generate_bibliography()