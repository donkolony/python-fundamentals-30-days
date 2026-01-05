class PersonAccount:
    def __init__(self, firstname, lastname):
        # Person details
        self.firstname = firstname
        self.lastname = lastname

        # Store incomes and expenses as dictinaires
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        # Add income with a name and amount
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        # Add expense with a name and amount
        self.expenses[description] = amount

    def total_income(self):
        # Add all income values together
        total = 0
        for amount in self.incomes.values():
            total += amount

        return total

    def total_expense(self):
        # Add all expense values together
        total = 0
        for amount in self.expenses.values():
            total += amount

        return total

    def account_balance(self):
        # Money left after expense
        # Money in - Money out
        return self.total_income() - self.total_expense()

    def account_info(self):
        # Show account details nicely
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: R{self.total_income()}\n"
            f"Total Expense: R{self.total_expense()}\n"
            f"Account Balance: R{self.account_balance()}"
        )
