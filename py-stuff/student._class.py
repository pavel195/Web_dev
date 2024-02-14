import random
base = {'IT': 260,
        "MED": 240,
        'Engenir' : 219}


class Abitu:
    def __init__(self, name, facult):
        self.name = name
        self.facult = facult
        self.scoreEGE = random.randint(100,300)
        self.counter = 0
    def display(self):
        print(self.name,self.facult,self.scoreEGE)
        self.counter += 1
    def display(self):
        print(self.name,self.facult,self.scoreEGE)
        self.counter += 1
    def __score_ege(self):
        print(f'{self.name} has {self.scoreEGE}')
        self.counter += 1
    def call_score_ege(self):
        self.__score_ege()
class Student(Abitu):
    vyzName = ''
    facs = ''

class Vyz:
    facs_and_places = {}
    prosh = {}
    def __init__(self, name):
        self.name = name


def set_places(vyz,facs):
    for i in range(len(facs)):
        vyz.facs_and_places[facs[i]] = random.randint(10,15)




def bubbleSort(array):
    l = len(array)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if array[j].scoreEGE < array[j + 1].scoreEGE:
                array[j].scoreEGE,array[j+1].scoreEGE = array[j+1].scoreEGE,array[j].scoreEGE
    return array

if __name__ =='__main__':
    vyz1 = Vyz('MIIT')
    namesMass = ['Vlad', 'Maksim', 'Oleg', 'Pavel', 'Anton', 'Aleksei', 'Aleksandr', 'Diana']
    facs = ['IT', 'Lingv', 'Eco']
    #создание список абитуриентов
    AllAbi = []
    for i in range(0,60):
        nameA = namesMass[random.randint(0,len(namesMass) - 1)]
        facA = facs[random.randint(0, len(facs) - 1)]
        AllAbi.append(Abitu(nameA, facA))
    #разделение абитуриентов по факультетам
    facsAbi = {} #абитуриенты как значение, факультет ключ
    for i in range(0, len(facs)):
        massAbiFac = []
        for k in range(0, len(AllAbi)):
            if AllAbi[k].facult == facs[i]:
                massAbiFac.append(AllAbi[k])
        facsAbi[facs[i]] = [massAbiFac]
    #сортировка абитуриентов по баллам на своих факультетах
    for i in range(0, len(facs)):
        facsAbi[facs[i]] = bubbleSort(facsAbi[facs[i]][0])

    for i in range(0, len(facs)):
        vyz1.facs_and_places[facs[i]] = random.randint(1,5)

    students = {}
    for i in range(0, len(facs)):
        places = vyz1.facs_and_places[facs[i]]
        abitur = facsAbi[facs[i]]
        massSt = []
        for k in range(0, places):
            AllAbi[k].__class__ = Student  #меняю класс абитуреента на дочерний клас студента, типо крутой
            AllAbi[k].facs = facs[i]
            AllAbi[k].vyzName = vyz1.name
            massSt.append(AllAbi[k])
        students[facs[i]] = massSt
    for i in range(0, len(facs)):
        print(facs[i] + ": \n")
        for k in range(0, len(facsAbi[facs[i]])):
            print(f'{k + 1})', end='')
            facsAbi[facs[i]][k].display()
    print("Поступили:")
    for i in range(0, len(facs)):
        print(f'{facs[i]} c количеством мест {vyz1.facs_and_places[facs[i]]}' + ": \n")
        for k in range(0, len(students[facs[i]])):
            print(f'{k+1})',end='')
            students[facs[i]][k].display()
            # students[facs[i]][k].__score_ege()
            students[facs[i]][k].call_score_ege()

