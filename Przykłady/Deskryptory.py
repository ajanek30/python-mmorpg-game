class Wallet:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return f"{self._balance:.2f} PLN"

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Saldo nie może być ujemne!")
        self._balance = value


account = Wallet(-5)
account.balance = 50
print(account.balance)

