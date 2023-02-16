class BankAccount:
    No_of_customers = 0
    account_num = 42010

    def __init__(self, name, mobile_no, initial_deposit, pin):

        self.name = name
        self.cust_acc_num = BankAccount.account_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_deposit
        self.pin = pin

        BankAccount.account_num = BankAccount.account_num + 1
        BankAccount.No_of_customers = BankAccount.No_of_customers + 1

    def basic_details(self):
        print(f"User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: INR {self.acc_balance}")

    def deposit(self):
        amount = int(input("Enter the deposit amount: "))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(f"Transaction completed. Current balance: INR {self.acc_balance}")
        else:
            print("Invalid amount transaction aborted")

    def withdrawal(self):
        amount = int(input("Enter The withdrawal amount"))
        if 0 < amount < self.acc_balance:
            self.acc_balance = self.acc_balance - amount
            print(f"Transaction completed. Current Balance: INR {self.acc_balance}")
        else:
            print("Invalid amount Transaction aborted")

    def payment(self, other):
        amount = int(input("Enter the payment amount"))
        if 0 < amount <= self.acc_balance:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(f"Transaction completed. Current Balance: INR {self.acc_balance}")
        else:
            print("Invalid amount transaction aborted")


cust1 = BankAccount(name="Ishan", mobile_no=9898989898, initial_deposit=1000, pin=1234)
cust2 = BankAccount(name="gill", mobile_no=9695969596, initial_deposit=1500, pin=5231)
# print(cust1.basic_details())


cust1.withdrawal()
print(cust1.payment(cust2))
