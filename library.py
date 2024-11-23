import os
import json
import datetime

from book import Book


# Класс для управления библиотекой
class Library:
    DATABASE_FILE = "library.json"

    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Функция загрузки книги из JSON-файла"""
        if not os.path.exists(self.DATABASE_FILE):
            return []
        with open(self.DATABASE_FILE, "r") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]

    def generate_id(self):
        """Функция генерации уникального идентификатора для книги"""
        return max((book.id for book in self.books), default=0) + 1

    def save_books(self):
        """Функция сохранения книги в JSON-файл"""
        with open(self.DATABASE_FILE, "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4, ensure_ascii=False)

    def add_book(self, title: str, author: str, year: str):
        """Функция добавления книги в библиотеку"""
        if int(year) > datetime.datetime.now().year:
            print(f"Книга '{title}' из будущего. Попробуйте заново.")
        else:
            book = Book(self.generate_id(), title, author, year)
            self.books.append(book)
            self.save_books()
            print(f"Книга '{title}' успешно добавлена.")

    def delete_book(self, book_id: int):
        """Функция удаления книги по ID"""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, query: str, field: str):
        """Функция поиска книги по указанному полю"""
        results = [book for book in self.books if query.lower() in getattr(book, field.lower())]
        if not results:
            print(f"Книга с {field} '{query}' не найдена.")
        else:
            self.display_books(results)

    def display_books(self, books=None):
        """Функция отображения библиотеки"""
        books = books or self.books
        if not books:
            print("В библиотеке нет книг.")
            return
        print(f"{'ID':<5} {'Название':<50} {'Автор':<30} {'Год':<5} {'Статус':<10}")
        print("-" * 105)
        for book in books:
            print(f"{book.id:<5} {book.title:<50} {book.author:<30} {book.year:<5} {book.status:<10}")

    def find_book_by_id(self, book_id: int):
        """Функция поиска книги по ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def update_status(self, book_id: int, new_status: str):
        """Функция обновления статуса книги"""
        if new_status not in ["в наличии", "выдана"]:
            print("Некорректный статус. Используйте 'в наличии' или 'выдана'.")
            return
        book = self.find_book_by_id(book_id)
        if book:
            book.status = new_status
            self.save_books()
            print(f"Статус книги с ID {book_id} обновлён на '{new_status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
