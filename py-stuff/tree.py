with open('file.txt', 'r') as file:
    lst = []

    while True:
        line = file.readline()
        line = line.split()  # надо вывести пирамидой по уровню
        if not line :
            break
        lst.append(line)
    i = 0
    while i <=len(lst):
        print(lst[i])
        i += int(lst[i])
        for j in range(i+1,int(lst[i][1])+1):
            print(lst[j],end=' ')
        i += int(lst[i][1])


