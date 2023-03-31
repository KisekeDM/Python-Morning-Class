class BankAccount:
    def balance(self):
        print("deposit", "withdraw", "checkbalance", "transfer")


class InterestAccount(BankAccount):
    def account(self):
        print("interest", "deposit")


class ChargingAccount(BankAccount):
    def charging(self):
        print("fee", "withdraw")


c = ChargingAccount()
c.balance()
c.charging()
