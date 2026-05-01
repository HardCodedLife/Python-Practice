class BankAccount:
    def __init__(self, n = 0) -> None:
        self.__balance = n
    def deposit(self, money):
        self.__balance += money
        print(f"Deposited {money}.")
        print(f"New Balance: {self.__balance}")
    def withdraw(self, money):
        if self.__balance < money:
            print(f"Insufficient funds! Final Balance: {self.__balance}")
            return
        self.__balance -= money
        print(f"Withdrew {money}.")
        print(f"New Balance: {self.__balance}")
if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(200) # This should trigger a warning
    account.withdraw(10) 
