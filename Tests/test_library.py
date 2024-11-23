import pytest
from library import Library


@pytest.fixture
def library():
    """Создание экземпляра библиотеки для тестов"""
    lib = Library()
    # Удаление данных перед каждым тестом
    lib.books = []
    lib.save_books()
    return lib

def test_add_book(library):
    """Тест на добавление книги"""
    library.add_book("Тестовая книга", "Тестовый автор", "2023")
    assert len(library.books) == 1
    assert library.books[0].id == 1
    assert library.books[0].title == "Тестовая книга"
    assert library.books[0].author == "Тестовый автор"
    assert library.books[0].year == "2023"
    assert library.books[0].status == "в наличии"

def test_delete_book(library):
    """Тест на удаление книги"""
    library.add_book("Удаляемая книга", "Автор", "2022")
    book_id = library.books[0].id
    library.delete_book(book_id)
    assert len(library.books) == 0

def test_delete_nonexistent_book(library, capsys):
    """Тест на удаление несуществующей книги"""
    library.delete_book(999)
    captured = capsys.readouterr()
    assert "Книга с ID 999 не найдена." in captured.out

def test_search_books_by_title(library):
    """Тест на поиск книги по названию"""
    library.add_book("Книга 1", "Автор 1", "2001")
    library.add_book("Книга 2", "Автор 2", "2002")
    results = [book.to_dict() for book in library.books if "Книга 1" in book.title]
    assert len(results) == 1
    assert results[0]["title"] == "Книга 1"

def test_update_status(library):
    """Тест на обновление статуса книги"""
    library.add_book("Книга для обновления", "Автор", "2020")
    book_id = library.books[0].id
    library.update_status(book_id, "выдана")
    assert library.books[0].status == "выдана"

def test_update_status_invalid(library, capsys):
    """Тест на обновление статуса с некорректным значением"""
    library.add_book("Книга", "Автор", "2020")
    book_id = library.books[0].id
    library.update_status(book_id, "неизвестно")
    captured = capsys.readouterr()
    assert "Некорректный статус. Используйте 'в наличии' или 'выдана'." in captured.out
    assert library.books[0].status == "в наличии"

def test_display_books_empty(library, capsys):
    """Тест на отображение книг при пустой библиотеке"""
    library.display_books()
    captured = capsys.readouterr()
    assert "В библиотеке нет книг." in captured.out
