# Question 2
class BankAccount:
    def __init__(self, bank_name, owner_name, acc_num, balance):
        self.bank_name = bank_name
        self.owner_name = owner_name
        self.acc_num = acc_num
        self.balance = balance

    def deposit_money(self, amount):
        self.balance += amount

    def withdraw_money(self, amount):
        if self.balance < amount:
            return None
        self.balance -= amount

    def print_status(self):
        print("Your Balance is " + str(self.balance))


chatchai = BankAccount("Big bank", "Chatchai", 123456, 1000)
chatchai.deposit_money(100)
chatchai.print_status()
chatchai.withdraw_money(200)
chatchai.print_status()
