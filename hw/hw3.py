class LibraryBook:
    def __init__(self, title, secret_code):
        self.title = title
        self._is_taken = False
        self.__secret_code = secret_code

    def take_book(self, code):
        if self._is_taken:
            print(f"Книгу '{self.title}' уже взяли ")
        elif code == self.__secret_code:
            self._is_taken = True
            print(f"Книга '{self.title}' успешно взяли.")
        else:
            print("Неверный секретный код. книгу не дааам.")

    def return_book(self):
        if self._is_taken:
            self._is_taken = False
            print(f"Книгу '{self.title}' вернули.")
        else:
            print(f"Книга '{self.title}' и так в библиотеке.")

book = LibraryBook("Преступление и наказание", "123")
book.take_book("wrong")
book.take_book("123")
book.return_book()


from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплачено {amount} сом. через банковскую карту.")

    def refund(self, amount):
        print(f"Возврат {amount} сом. на банковскую карту.")


class CryptoPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплачено {amount} биток через криптовалюту.")

    def refund(self, amount):
        print(f"Возврат {amount} биток через криптовалюту.")

card = CardPayment()
crypto = CryptoPayment()

card.pay(1500)
card.refund(500)

crypto.pay(0.03)
crypto.refund(0.01)

