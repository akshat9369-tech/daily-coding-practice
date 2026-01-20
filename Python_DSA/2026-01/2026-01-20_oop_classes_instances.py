"""OOP: Classes, Objects, Attributes, and __init__."""

class BankAccount:
    bank_name = "Global Dev Bank"  # Class attribute

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_statement(self) -> str:
        return f"[{self.bank_name}] Holder: {self.holder} | Balance: ${self.balance:.2f}"

if __name__ == "__main__":
    acc = BankAccount("Akshat", 500.0)
    print(acc.get_statement())
    acc.deposit(250.0)
    acc.withdraw(120.0)
    print(acc.get_statement())
