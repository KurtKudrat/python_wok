class Employee():

    def __init__(self,first_name,last_name,annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_amount= ''):
        if raise_amount:
            self.annual_salary = self.annual_salary +raise_amount
            return self.annual_salary
        else:
            self.annual_salary = self.annual_salary + 5000
            return self.annual_salary
