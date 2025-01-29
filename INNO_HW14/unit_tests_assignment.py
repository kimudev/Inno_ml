import pytest
from unittest.mock import MagicMock

# --- Задача 1: Тестирование методов класса BooksCollector ---
class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
    
    def add_new_book(self, book_name):
        self.books_genre[book_name] = None
    
    def set_book_genre(self, book_name, genre):
        if book_name in self.books_genre:
            self.books_genre[book_name] = genre
    
    def get_book_genre(self, book_name):
        return self.books_genre.get(book_name)
    
    def add_book_in_favorites(self, book_name):
        if book_name in self.books_genre and book_name not in self.favorites:
            self.favorites.append(book_name)
    
    def delete_book_from_favorites(self, book_name):
        if book_name in self.favorites:
            self.favorites.remove(book_name)
    
    def get_list_of_favorites_books(self):
        return self.favorites

# --- Тесты для BooksCollector ---
class TestBooksCollector:
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        assert "Властелин колец" in collector.books_genre

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фэнтези")
        assert collector.get_book_genre("Гарри Поттер") == "Фэнтези"

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Матрица")
        collector.add_book_in_favorites("Матрица")
        assert "Матрица" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Матрица")
        collector.add_book_in_favorites("Матрица")
        collector.delete_book_from_favorites("Матрица")
        assert "Матрица" not in collector.get_list_of_favorites_books()

# --- Задача 2: Работа с мок-объектами ---
class CreditCard:
    def __init__(self, number, holder, expiry, cvv):
        self.number = number
        self.holder = holder
        self.expiry = expiry
        self.cvv = cvv
    
    def charge(self, amount):
        return f"Charged {amount} successfully"

class PaymentForm:
    def __init__(self, credit_card):
        self.credit_card = credit_card
    
    def pay(self, amount):
        return self.credit_card.charge(amount)

# --- Тесты с мок-объектами ---
class TestPaymentForm:
    def test_payment_success(self):
        mock_card = MagicMock()
        mock_card.charge.return_value = "Charged 100 successfully"
        payment_form = PaymentForm(mock_card)
        assert payment_form.pay(100) == "Charged 100 successfully"

    def test_payment_failure(self):
        mock_card = MagicMock()
        mock_card.charge.side_effect = Exception("Payment failed")
        payment_form = PaymentForm(mock_card)
        with pytest.raises(Exception, match="Payment failed"):
            payment_form.pay(200)