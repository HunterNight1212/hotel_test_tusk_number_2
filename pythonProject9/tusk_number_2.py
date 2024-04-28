import random



def del_1(list_=list):
    list_ = list(map(int, input('enter your numbers please: ').split()))
    list_2 = []
    while len(list_) != len(list_2):
        for i in list_:
            v = i / random.randint(2, 9)
            v = int(v)
            if all(element % v == 0 for element in list_):
                if v in list_2 or v == 1:
                    continue
                else:
                    list_2.append(v)
                print(list_2)



del_1()
