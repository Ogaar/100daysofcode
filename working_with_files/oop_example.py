class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


# Example usage
account1 = BankAccount("1234567890", "John Doe", 1000.0)
account1.display_account_details()
account1.deposit(500.0)
account1.withdraw(200.0)
print("Current Balance:", account1.get_balance())

# Example 2
account2 = BankAccount("5858585858", "Fred Borden", 1000000000.0)
if account2.balance > account1.balance:
    print("Fred is richer than John.")
else:
    print("Fred is poor.")

account2_money = account2.get_balance()
account1_money = account1.get_balance()
if account2_money > account1_money:
    print("Fred is richer than John.")
else:
    print("Fred is poor.")

