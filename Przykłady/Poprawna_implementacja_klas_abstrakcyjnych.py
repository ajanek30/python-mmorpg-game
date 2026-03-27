from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Przetworzono {amount} przez Stripe")


class FakeProcessor(PaymentProcessor):
    pass


p1 = StripeProcessor().process_payment(12)

#p2 = FakeProcessor() Wyrzuca błąd!!!

