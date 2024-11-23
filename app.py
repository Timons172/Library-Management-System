from library import Library


# Класс для управления интерфейсом командной строки
class LibraryApp:
    def __init__(self):
        self.library = Library()

    def menu_add_book(self):
        """Функция меню - 1 по добавлению в библиотеку книги"""
        try:
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            year = input("Введите год издания: ").strip()
            self.library.add_book(title, author, year)
        except ValueError:
            print("Год издания должен быть числом. Попробуйте заново.")

    def menu_delete_book(self):
        """Функция меню - 2 по удалению книги из библиотеки по ID"""
        try:
            book_id = int(input("Введите ID книги для удаления: ").strip())
            self.library.delete_book(book_id)
        except ValueError:
            print("ID книги должен быть числом. Попробуйте заново.")

    def menu_search_book(self):
        """Функция меню - 3 по поиску книги в библиотеке по названию, автору или году издания"""
        field = input("Как будем искать книгу? По 'title', 'author' или 'year': ").strip()
        if field.lower() in ["title", "author", "year"]:
            query = input("Введите значение для поиска: ").strip()
            self.library.search_books(query, field)
        else:
            print("Необходимо ввести поле для поиска: 'title', 'author' или 'year'. Повторите заново.")

    def menu_show_library(self):
        """Функция меню - 4 по отображению всей библиотеки"""
        self.library.display_books()

    def menu_change_status(self):
        """Функция меню - 5 по изменению статуса книги"""
        try:
            book_id = int(input("Введите ID книги для изменения статуса: ").strip())
            new_status = input("Введите новый статус ('в наличии' или 'выдана'): ").lower().strip()
            self.library.update_status(book_id, new_status)
        except ValueError:
            print("ID книги должен быть числом.")

    def run(self):
        """Функция основного цикла приложения"""
        while True:
            print(f"\nМеню библиотеки книг:\n"
                  f"1 - Добавить книгу\n"
                  f"2 - Удалить книгу\n"
                  f"3 - Искать книгу\n"
                  f"4 - Отобразить всю библиотеку\n"
                  f"5 - Изменить статус книги\n"
                  f"6 - Выход")
            choice = input("Выберите пункт меню: ").strip()
            match choice:
                case "1":
                    self.menu_add_book()
                case "2":
                    self.menu_delete_book()
                case "3":
                    self.menu_search_book()
                case "4":
                    self.menu_show_library()
                case "5":
                    self.menu_change_status()
                case "6":
                    print("Выход из программы.")
                    break
                case _:
                    print("Некорректный пункт меню. Попробуйте заново.")
