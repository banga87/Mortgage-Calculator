import time

class Person:
    
    def __init__(self, name=None, monthly_salary=None, monthly_expenses=None):
        if not name:
            self.name = input("Enter your name: ")
        else:
            self.name = name

        if not monthly_salary:
            self.monthly_salary = input("What is your monthly salary?: ")
        else:
            self.monthly_salary = monthly_salary

        if not monthly_expenses:    
            self.monthly_expenses = input("What are your monthly expenses?: ")

        self.mortgage = None
        self.monthly_budget = None

    def monthly_budget(self):
        self.monthly_budget = self.monthly_salary - self.monthly_expenses

class Mortgage:
    
    def __init__(self, rate=0.0362, principal=None, term=None):
        self.rate = rate

        if not principal:
            self.principal = input("How much are you looking to borrow?: ")
        else:
            self.principal = principal

        if not term:
            self.term = input("How many years would you like to lock the loan in for?: ")
        else:
            self.term = term

    def monthly_rate(self):
        monthly_rate = self.rate / 12
        return monthly_rate

    def num_monthly_payments(self):
        num_monthly_payments = self.term * 12
        return num_monthly_payments

    def monthly_payments(self):
        numerator = self.principal(1 + self.monthly_rate)**self.num_monthly_payments
        denominator = ((1 + self.monthly_rate)**self.num_monthly_payments) - 1
        monthly_payments = numerator / denominator
        return monthly_payments




print(" ::: Welcome to Mortgage Calculator v1 ::: ")
print("Please provide the information prompted below")
p = Person()
m = Mortgage()
monthly_rate = m.monthly_rate()
num_monthly_payments = m.num_monthly_payments()
monthly_payments = m.monthly_payments()
monthly_budget = p.monthly_budget()
print("Your monthly repayments would be ${}.".format(monthly_payments))
print("We're just running some numbers... hang tight...")
time.sleep(3)

if monthly_payments >= p.monthly_budget:
    print("You're out of your fucking mind mate.")
    print("There is no way we are approving you for this loan!")
else:
    print("Loan application has been approved.")


