class BankAccount:
    def __init__(self, owner, initial_balance=0.0):
        # YOUR CODE HERE
        pass
    def deposit(self, amount):
        # YOUR CODE HERE
        pass
    def withdraw(self, amount):
        # YOUR CODE HERE
        pass
    def apply_interest(self, rate):
        # YOUR CODE HERE
        pass
    def get_balance(self):
        # YOUR CODE HERE
        pass
    def get_owner(self):
        # YOUR CODE HERE
        pass
    def is_rich(self):
        # YOUR CODE HERE
        pass
    def get_transaction_count(self):
        # YOUR CODE HERE
        pass
    def get_history(self):
        # YOUR CODE HERE
        pass
    
    
if __name__ == "__main__":
    # Create an account
    acc = BankAccount("Maria", 500.0)
    print(f"Owner: {acc.get_owner()}") # Maria
    print(f"Balance: ${acc.get_balance()}") # 500.0
    print(f"Rich? {acc.is_rich()}") # False
    # Make deposits and withdrawals
    acc.deposit(150.0)
    acc.withdraw(50.0)
    acc.deposit(25.0)
    print(f"New balance: ${acc.get_balance()}") # 625.0
    print(f"Transactions: {acc.get_transaction_count()}") # 3
    # Apply interest (5%)
    acc.apply_interest(0.05)
    print(f"After interest: ${acc.get_balance()}") # 656.25
    # Check history
    print("\nTransaction history:")
    for entry in acc.get_history():
        print(" " + entry)
    # Test rich status
    rich_acc = BankAccount("Jeff", 2_000_000)
    print(f"\nJeff rich? {rich_acc.is_rich()}") # True