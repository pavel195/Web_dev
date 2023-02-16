import random
base = {'IT': 260,
        "MED": 240,
        'Engenir' : 219}


class Abitu:
    def __init__(self, name, facult):
        self.name = name
        self.facult = facult
        self.scoreEGE = random.randint(100,300)
    def display(self):
        print(self.name,self.facult,self.scoreEGE)


class Student(Abitu):
    def __init__(self,abi,vyzName,facs):
        self.name = abi.name
        self.facult = abi.facult
        self.scoreEGE = abi.scoreEGE
        self.vyzName = vyzName
        self.facs = facs





class Vyz:
    facs_and_places = {}
    def __init__(self, name):
        self.name = name


# def set_places(vyz,facs):
#     for i in range(len(facs)):
#         vyz.facs_and_places[facs[i]] = random.randint(10,15)


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
        nameA = namesMass[random.randint(0,len(namesMass))-1]
        facA = facs[random.randint(0, len(facs) - 1)]
        AllAbi.append(Abitu(nameA, facA))
    #разделение абитуриентов по факультетам
    facsAbi = {} #абитуриенты как значение, факультет ключ
    for i in range(0, len(facs)):
        massAbiFac = [] #массив абитурентов по факультетам
        for k in range(0, len(AllAbi)):
            if AllAbi[k].facult == facs[i]:
                massAbiFac.append(AllAbi[k])
        facsAbi[facs[i]] = massAbiFac
    #сортировка абитуриентов по баллам на своих факультетах
    for i in range(0, len(facs)):
        print(type(facs[i][0]))
        print(type(facsAbi[facs[i]]))
        #print([x.scoreEGE for x in facsAbi[facs[i]][0] ])
        facsAbi[facs[i]] = sorted(facsAbi[facs[i]], key = lambda x: x.scoreEGE, reverse= True)
        #
        #[facs[i]] = bubbleSort(facsAbi[facs[i]][0])

    for i in range(0, len(facs)):
        vyz1.facs_and_places[facs[i]] = random.randint(1,5)

    # for i in range(0,len(facs)):
    #     for k in range(0,len(facsAbi[facs[i]])):
    #         facsAbi[facs[i]][k].display()

    students_and_facs = {}
    for i in range(0, len(facs)):
        places = vyz1.facs_and_places[facs[i]]
        abitur = facsAbi[facs[i]]
        massSt = [] # массив студентов которые прошли отбор
        for k in range(0, places):
            facsAbi[facs[i]][k] = Student(facsAbi[facs[i]][k],vyz1.name,facs[i])
            # facsAbi[facs[i]][k].facs = facs[i]
            # facsAbi[facs[i]][k].vyzName = vyz1.name
            massSt.append(facsAbi[facs[i]][k]) # записываем в студенты абитуриента
        students_and_facs[facs[i]] = massSt

    for i in range(0, len(facs)):
        print(facs[i] + ": ")
        for k in range(0, len(facsAbi[facs[i]])):
            facsAbi[facs[i]][k].display()
    print("Поступили:")
    for i in range(0, len(facs)):
        print(f'{facs[i]} c количеством мест {vyz1.facs_and_places[facs[i]]}' + ": ")
        for k in range(0, len(students_and_facs[facs[i]])):
           students_and_facs[facs[i]][k].display()

