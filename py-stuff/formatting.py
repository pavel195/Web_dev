class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: %s, age : %d' %(self.name, self.age) +'\n' + \
               'Name : {0.name} and age: {0.age}'.format(self) + '\n' + \
               f'Name: {self.name}, age : {self.age *2 }'
    # def display(self):
    #     try:
    #         assert self.age<18, "Вы достигли совершенолетия"
    #         self.age = self.age / 0
    #     except ZeroDivisionError:
    #         print('деление на ноль')
try :
    vasya = Person('Vasya', 39)
    #assert vasya.age < 18,"Вы достигли совершенолетия"
    # print([vasya.name[i] for i in range(10)])
    # vasya = vasya.age / 0
    #vasya.age + vasya.name
    #int(vasya.name)
except ZeroDivisionError:
    print('деление на ноль')
except (KeyError, IndexError):
    print('не тот ключ в словаре или не тот индекс')
except ValueError:
    print('Нельзя конвертировать в integer')
except TypeError:
    print('нельзя совмещать несовместимые типы ')
else:
    print('нет ошибок ')
finally:
    print('выполняется в любом случае')
