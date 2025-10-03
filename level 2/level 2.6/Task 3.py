numbers_list = [1, 2, 3, 4, 5, 6]
complite_list = []
good_list = []
index1 = 0
index2 = 1

for i in numbers_list:
    for j in numbers_list:
        if index1 % 2 == 0:
            i = str(i)
            index1 += 2
        elif index2 % 2 == 1:
            j = str(j)
            index2 += 2
            good_list.append(i, j)
        good = ''.join(good_list)
        complite_list.append(good)

print(complite_list)
