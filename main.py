import random

def ask_again(prompt):
    while True:
        answer = input(prompt)
        if answer in ("yes" , "no"):
            return answer
        print("Answer must be yes or no!")

class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("Invalid Amount!")
            return
        self.balance += deposit_amount
        print("Your Amount Has Been Deposited!")
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Withdraw Amount Is Higher Than Balance")
            return
        if withdraw_amount <= 0:
            print("Invalid Amount!")
            return
        self.balance -= withdraw_amount
        print("Your Amount Has Been Withdrawn!")
    def display_info(self):
        print(f"Account Holder: {self.account_holder}\n"
              f"Account Number: {self.account_number}\n"
              f"Balance: {self.balance}\n")

def main():
    print("Welcome to Bank Account Manager!".center(40,"="))
    print("\n")
    accs = []
    try:
        while True:
            name = input("Enter Your Account Holder: ").capitalize().strip()
            while not name:
                name = input("Enter Your Account Holder: ").capitalize().strip()
            acc_no = random.randint(1, 999999)
            account_object = BankAccount(name, acc_no)
            accs.append(account_object)
            if ask_again("Do you want to add another account?(yes,no): ") != "yes":
                break
        while True:

            menu = """
                1. Deposit
                2. Withdraw
                3. Display Info
                4. Display All Accounts
                5. Exit
            """
            print(menu)
            found = False

            try:
                option = int(input("Enter your choice(1-5): "))
            except ValueError:
                print("Invalid Input!")
                continue


            if option == 1:
                name = input("Enter Your Account Holder: ").strip().capitalize()
                for acc in accs:
                    if acc.account_holder == name:
                        found = True
                        try:
                            deposit_amount = int(input("Enter your deposit amount: "))
                        except ValueError:
                            print("Invalid Input!")
                            continue
                        acc.deposit(deposit_amount)
                if not found:
                    print("Account Holder Does Not Exist!")
                    continue

            elif option == 2:
                name = input("Enter Your Account Holder: ").strip().capitalize()
                for acc in accs:
                    if acc.account_holder == name:
                        found = True
                        try:
                            withdraw_amount = int(input("Enter your withdraw amount: "))
                        except ValueError:
                            print("Invalid Input!")
                            continue
                        acc.withdraw(withdraw_amount)
                if not found:
                    print("Account Holder Does Not Exist!")
                    continue

            elif option == 3:
                name = input("Enter Your Account Holder: ").strip().capitalize()
                for acc in accs:
                    if acc.account_holder == name:
                        found = True
                        acc.display_info()
                if not found:
                    print("Account Holder Does Not Exist!")
                    continue

            elif option == 4:
                for acc in accs:
                    acc.display_info()

            elif option == 5:
                print("Thank you for using this program!")
                break

            else:
                print("Please Choose Option Between 1-5!")
                continue


    except ValueError:
        print("Invalid Input!")

if __name__ == "__main__":
    main()