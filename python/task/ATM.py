user_data = {
    "sheljin" : 0000,
    "joel"    : 3813,
    "sree"    : 1234,
    "shyju"   : 1111,
    "jerin"   : 1510
}
user_balance = {
    "sheljin" : 100,
    "joel"    : -105,
    "sree"    : 1000,
    "shyju"   : 1000,
    "jerin"   : 50
}

class ATMMachine:
    def __init__(self):
        self.user_name = input("Enter user name: ")
        self.user_pass = input("Enter pass: ")
        self.user_check()

    def user_check(self):
        if self.user_name.lower() == "c" or self.user_pass.lower() == "c":
            self.cancel()
            return
        elif self.user_name in user_data and user_data[self.user_name] == int(self.user_pass):
            self.transaction()
        else:
            print("Invalid username or password")
            self.__init__()

    def transaction(self):
        self.trans_type = input("Enter\n'd' to debit\n'a' to credit\n'b' to check balance\n").lower()
        self.check_trans_mode()

    def cancel(self):
        print("Transaction cancelled\nThank you")

    def check_trans_mode(self):
        if self.trans_type == 'c':
            self.cancel()
        elif self.trans_type == 'd':
            self.debit()
        elif self.trans_type == 'a':
            self.credit()
        elif self.trans_type == 'b':
            self.balance()
        else:
            print("Invalid input, please try again.")
            self.transaction()

    def debit(self):
        debit_amount = input("Enter the amount to debit: ").lower()
        
        if debit_amount == 'c':
            self.cancel()
            return
        
        else:
            debit_amount = int(debit_amount)

        if user_balance[self.user_name] >= debit_amount:
            user_balance[self.user_name] -= debit_amount
            self.check_balance()

        else:
            print("Amount exceeded the balance")
            self.check_balance()

    def credit(self):
        credit_amount = input("Enter the amount to credit: ").lower()

        if credit_amount == 'c':
            self.cancel()
            return
        else:
            credit_amount = int(credit_amount)

        user_balance[self.user_name] += credit_amount
        self.check_balance()

    def check_balance(self):
        check_bal = input("Type 'y' to show balance\nType 'n' to exit\n").lower()
        if check_bal == 'y':
            self.balance()

        elif check_bal == 'c':
            self.cancel()

        else:
            self.thankyou()

    def balance(self):
        print(f"Your balance is {user_balance[self.user_name]}rs")
        self.thankyou()

    def thankyou(self):
        print("Thank you for using the ATM😊")

atm = ATMMachine()