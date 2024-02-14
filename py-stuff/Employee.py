
import random
def podschet(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f'---Функция {func.name} выполнилась {wrapper.count} раз---')
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

class Employee:
    empCount = 0
    #@podschet
    def __init__(self, name, salary,company):
        self.name = name
        self.salary = salary
        self.company = company
        Employee.empCount += 1
    #@podschet
    def displayCount(self):
        print(f"Total Employee  {Employee.empCount}")
    #@podschet
    def displayEmployee(self):
        print(f"Name :  {self.name} , Salary {self.salary}")

class Company:
    #@podschet
    def __init__(self,name, max_salary):
        self.name = name
        self.max_salary = max_salary
    #@podschet
    def displayComplany(self):
        print(f'Company {Company.name} can pay to employees {Company.max_salary}')

if __name__ == '__main__':
    names = ['Sasha', 'Misha','Georg','Peter']
    companies = ['Yandex', 'Google']
    employers = []
    for i in range(10):
        salaryE = random.randint(0,10000000000)
        nameE = names[random.randint(0,len(names)-1)]
        companyE = companies[random.randint(0,len(companies)-1)]
        employers.append(Employee(nameE, salaryE,companyE))
    # for a in employers:
    #     print(a.displayEmployee())
    comp1 = Company('Yandex',random.randint(0,1000000))
    comp2 = Company('Google',random.randint(0,1000000))


