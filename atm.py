import time
import sys

class ATM:
    def __init__(self):
        self.account_no = None
        self.name = ""
        self.pin = None
        self.balance = 0.0
        self.mobile_no = ""
        self.transaction_history = []
        self.is_locked = False
        self.pin_attempts = 0

    def set_data(self, account_no, name, pin, balance, mobile_no):
        self.account_no = account_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.mobile_no = mobile_no

    def get_account_no(self):
        return self.account_no

    def get_name(self):
        return self.name

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def get_mobile_no(self):
        return self.mobile_no

    def get_transaction_history(self):
        return self.transaction_history

    def get_lock_status(self):
        return self.is_locked

    def set_mobile(self, old_mobile, new_mobile):
        if old_mobile == self.mobile_no:
            self.mobile_no = new_mobile
            print("\nSuccessfully Updated Mobile No.")
        else:
            print("\nIncorrect Old Mobile No!")

    def cash_withdraw(self, amount):
        if amount > 0 and amount <= self.balance and amount <= 20000:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print("\nPlease collect your cash")
            print(f"Available Balance: {self.balance}")
        elif amount > 20000:
            print("\nWithdrawal limit exceeded! You can only withdraw up to 20000.")
        else:
            print("\nInvalid input or insufficient balance")

    def lock_account(self):
        self.is_locked = True
        print("\nYour account has been locked due to multiple incorrect attempts.")

    def track_pin_attempts(self):
        self.pin_attempts += 1
        if self.pin_attempts >= 3:
            self.lock_account()

    def reset_pin_attempts(self):
        self.pin_attempts = 0

    def unlock_account(self):
        self.is_locked = False
        self.pin_attempts = 0
        print("\nYour account has been unlocked. Please try again with correct details.")

def main():
    users = []
    users.append(ATM())
    users[-1].set_data(987654321, "Ammar", 1234, 150000, "92370054900")
    users.append(ATM())
    users[-1].set_data(123456789, "Aadil", 4321, 30000, "92376543210")
    users.append(ATM())
    users[-1].set_data(555555555, "Rehman", 5678, 25000, "92323456789")
    users.append(ATM())
    users[-1].set_data(888888888, "Sara", 8765, 100000, "92301122334")

    for u in users:
        print(f"Account No: {u.get_account_no()} | PIN: {u.get_pin()} | Name: {u.get_name()}")

    while True:
        print("\n**** Welcome to ATM *****")
        try:
            enter_account_no = int(input("Enter Your Account No: "))
            enter_pin = int(input("Enter PIN: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        user = None
        for u in users:
            if enter_account_no == u.get_account_no() and enter_pin == u.get_pin():
                user = u
                break

        if user:
            if user.get_lock_status():
                print("Account is locked. Please contact support.")
                continue

            user.reset_pin_attempts()

            while True:
                print("\n**** Welcome to ATM *****")
                print("1. Check Balance")
                print("2. Cash Withdraw")
                print("3. Show User Details")
                print("4. Update Mobile No.")
                print("5. View Transaction History")
                print("6. Lock Account (for security purposes)")
                print("7. Exit")

                choice = input("Select an option: ")

                if choice == '1':
                    print(f"\nYour Bank Balance is: {user.get_balance()}")

                elif choice == '2':
                    try:
                        amount = int(input("Enter the amount: "))
                        user.cash_withdraw(amount)
                    except ValueError:
                        print("Invalid amount entered.")

                elif choice == '3':
                    print("\n*** User Details ***")
                    print(f"-> Account No: {user.get_account_no()}")
                    print(f"-> Name: {user.get_name()}")
                    print(f"-> Balance: {user.get_balance()}")
                    print(f"-> Mobile No.: {user.get_mobile_no()}")

                elif choice == '4':
                    old_mobile = input("Enter Old Mobile No.: ")
                    new_mobile = input("Enter New Mobile No.: ")
                    user.set_mobile(old_mobile, new_mobile)

                elif choice == '5':
                    print("\n*** Transaction History ***")
                    for transaction in user.get_transaction_history():
                        print(transaction)

                elif choice == '6':
                    user.lock_account()
                    break

                elif choice == '7':
                    print("Thank you for using the ATM!")
                    sys.exit()

                else:
                    print("Enter valid data!")

        else:
            print("\nUser details are invalid!")
            # Find user by account_no to track attempts and lock only that account
            found_user = next((u for u in users if enter_account_no == u.get_account_no()), None)
            if found_user:
                found_user.track_pin_attempts()
                if found_user.get_lock_status():
                    retry = input("Would you like to try again? (y/n): ")
                    if retry.lower() == 'y':
                        print("Please wait for 30 seconds before retrying...")
                        time.sleep(30)
                        found_user.unlock_account()
                        continue
                    else:
                        print("Exiting. Please try again later.")
                        break
            else:
                print("Account number not found.")

if __name__ == "__main__":
    main()
