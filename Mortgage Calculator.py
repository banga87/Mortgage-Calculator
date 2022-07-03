import time

class Person:
    
    def __init__(self, name=None, monthly_salary=None, monthly_expenses=None):
        if not name:
            self.name = input("Enter your name: ")
        else:
            self.name = name

        if not monthly_salary:
            self.monthly_salary = int(input("What is your monthly salary?: "))
        else:
            self.monthly_salary = monthly_salary

        if not monthly_expenses:    
            self.monthly_expenses = int(input("What are your monthly expenses?: "))

        self.mortgage = 0
        self.monthly_budget = 0

    def budget_calc(self):
        budget = self.monthly_salary - self.monthly_expenses
        self.monthly_budget = budget
        return self.monthly_budget

class Mortgage:
    
    def __init__(self, rate=0.0362, principal=None, term=None):
        self.rate = rate

        if not principal:
            self.principal = int(input("How much are you looking to borrow?: "))
        else:
            self.principal = principal

        if not term:
            self.term = int(input("How many years would you like to lock the loan in for?: "))
        else:
            self.term = term

    def monthly_rate(self):
        m_rate = float(self.rate / 12)
        return m_rate

    def num_monthly_payments(self):
        num_monthly_payments = int(self.term * 12)
        return num_monthly_payments

    def monthly_payments(self, m_rate, n_payments):
        numerator = m_rate*self.principal*(1 + m_rate)**n_payments
        denominator = ((1 + m_rate)**n_payments) - 1
        payments = numerator / denominator
        return payments




print(" ::: Welcome to Mortgage Calculator v1 ::: ")
print("Please provide the information prompted below")

p = Person()
m_budget = p.budget_calc()
print("Prospect Name: {}".format(p.name))
print("Prospect Salary: ${}".format(p.monthly_salary))
print("Prospect Expenses: ${}".format(p.monthly_expenses))
print('\n')

m = Mortgage()
print('\n')
print("Requested Principal: ${}".format(m.principal))
print("Requested Term: {}".format(m.term))

m_rate = m.monthly_rate()
print("Monthly Rate: {}".format(m_rate))

num_payments = m.num_monthly_payments()
print("Number of Payments: {}".format(num_payments))

m_payments = m.monthly_payments(m_rate, num_payments)
print("Monthly Payment Amount: {}".format(m_payments))
print('\n')

print("Your monthly repayments would be ${}.".format(m_payments))
print("We're just running some numbers... hang tight...")
time.sleep(3)

if m_payments >= m_budget:
    print("You're out of your fucking mind mate.")
    print("There is no way we are approving you for this loan!")
else:
    print("Loan application has been approved.")


