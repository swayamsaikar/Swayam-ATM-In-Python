import sys


class ATM(object):
    def __init__(self, CardNumber, PinNumber, Cash):
        self.CardNumber = CardNumber
        self.PinNumber = PinNumber
        self.Cash = Cash

    def cashWithDrawl(self):
        withdrawAmount = int(input("Enter The Amount You Want To WithDraw\n"))
        if withdrawAmount > self.Cash:
            print(
                f"Your Current amount is {self.Cash} and you told to withdraw {withdrawAmount}\n")
            print(
                f"Please give amount less than your current balance : {self.Cash}\n")

            sys.exit(101)
        else:

            BalanceLeft = self.Cash - withdrawAmount
            self.Cash = BalanceLeft
            return f"Total Balance Left in Account: {BalanceLeft}\n"

    def AccessDetails(self):
        question = input("Do You Want To See Your Details ?\n")
        if(question == "yes" or "Yes" or "ya" or "Ya" or "Yeah" or "yeah" or "yep" or "Yep"):

            print(f"CardNumber : {self.CardNumber}")
            print(f"PinNumber : {self.PinNumber}")
            print(f"Total Cash Left In Your Account : {self.Cash}")
            print("Thankyou For Using Swayam ATM")
            sys.exit(101)

        else:
            print("Thankyou For Using Swayam ATM!")
            sys.exit(101)


# initialized the class with a variable
atm = ATM(895757, 93887, 100)
print(atm.cashWithDrawl())
atm.AccessDetails()
