# Класс для представления книги
class Book:
    def __init__(self, book_id: int, title: str, author: str, year: str, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        """Функция преобразования объекта книги в словарь"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict):
        """Функция создания объекта книги из словаря"""
        return Book(data["id"], data["title"], data["author"], data["year"], data["status"])
