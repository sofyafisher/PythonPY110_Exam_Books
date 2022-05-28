import random
from faker import Faker

fake = Faker()
Faker.seed(0)


def author_gen() -> str:
    """Возвращает случайное количество (от 1 до 3) случайных имен"""
    lst_ = []
    amount = random.randint(1, 3)
    for _ in range(amount):
        lst_.append(fake.name())
    return ", ".join(lst_)


def title() -> str:
    """Возвращает случайную строку из файла books.txt"""
    lst_ = []
    filename = "books.txt"
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lst_.append(line)
    return random.choice(lst_)


def other_fields() -> dict:
    """Добавляет в словарь fields пару ключ-случайно сгенерированное значение """
    fields = {'title': title(),
              'year': random.randint(0, 2022),
              "pages": random.randint(0, 700),
              'isbn13': fake.isbn13(),
              'rating': round(random.uniform(0, 5), 2),
              "price": round(random.uniform(300, 30000), 2),
              "author": author_gen()
              }
    return fields
