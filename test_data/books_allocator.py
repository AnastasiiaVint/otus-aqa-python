import json
from csv import DictReader


def parser(read_file, fields):
    """Extract data based on the fields"""

    result_data = []
    i = 0
    for row in read_file:
        result_data.append({})
        for data in row:
            if data in fields:
                result_data[i][data.lower()] = row[data]
        i += 1
    return result_data


with open("files/books.csv", 'r', encoding='utf-8') as books_file:
    reader = DictReader(books_file)
    books_fields = ["Title", "Author", "Genre", "Pages"]
    books = parser(reader, books_fields)
    books_gen = (book for book in books)

    with open("files/users.json", "r", encoding='utf-8') as users_file:
        reader = json.loads(users_file.read())
        users_fields = ["name", "gender", "address", "age"]
        users = parser(reader, users_fields)
        while True:
            try:
                for user in users:
                    if not user.get("books"):
                        user["books"] = []
                    user["books"].append(next(books_gen))
            except StopIteration:
                break
        result = json.dumps(users, indent=4)

        with open("files/result.json", "w", encoding='utf-8') as result_file:
            result_file.write(result)
