class Person:
    
    def __init__(self, name, current_debt, monthly_salary, monthly_expenses):
        self.name = name
        self.current_debt = current_debt
        self.monthly_salary = monthly_salary
        self.monthly_expenses = monthly_expenses

class Mortgage:
    
    def __init__(self, rate, principal, term):
        self.rate = rate
        self.principal = principal
        self.term = term

    def monthly_rate(self):
        return self.rate / 12

    def num_monthly_payments(self):
        return self.term * 12

    def monthly_payments(self):
        pass