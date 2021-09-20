class atm:
    def __init__(self, atm_no, pin_no):
        self.atm_no = atm_no
        self.pin_no = pin_no

    def checkBalance(self):
        print("Your balance is 50000")

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print(f'You have withdrawn {amount} and you have {new_amount} left in your account')

def main():
    card_no = 123456
    pin_no = 7890
    new_user = atm(card_no, pin_no)
    new_user.checkBalance()
    amount = int(input("How much money do you want to withdraw : "))
    new_user.withdrawl(amount)

main()