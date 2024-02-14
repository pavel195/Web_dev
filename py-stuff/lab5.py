import matplotlib.pyplot as plt
import json
lst_x= [x for x in range(-10,11)]

def f1(x):
        return x*x-1
lst_y1 =[f1(x) for x in lst_x]

def f2(x):
        return x*x-8*x+15
lst_y2 = [f2(x) for x in lst_x]

def f3(x):
        return -2*x*x+4*x
lst_y3 = [f3(x) for x in lst_x]

plt.figure(1)
plt.title('график функций')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.plot(lst_x,lst_y1,'g.-')
plt.plot(lst_x,lst_y2,'.-')
plt.plot(lst_x,lst_y3,'.-')

plt.figure(2)

def f4(x):
        if x>=1:
                return x*x-6*x + 10
        else:
                pass
def f5(x):
        if x<=1:
                return x+2
        else:
                pass
plt.grid()
lst_y4 = [f4(x) for x in lst_x]
lst_y5 = [f5(x) for x in lst_x]
plt.plot(lst_x,lst_y4)
plt.plot(lst_x,lst_y5)
plt.show()

plt.figure(3)
with open('some.json','r',encoding='utf-8') as file:
        data = json.load(file)

employee_name = data['ФИО']
year = 2010
split_data = [x for x in data['Выплаты'] if x['Год'] == str(year) and employee_name in data['ФИО']]

# x
x_vales = [x['Месяц'] for x in split_data]
# y
y_values = [int(x['Размер выплаты']) for x in split_data]
plt.bar(x_vales,y_values)
plt.xlabel('Months')
plt.ylabel('salaries')
plt.title(f'Salaries for employe {employee_name} in {year} year')
plt.show()