list_num1 = range(1, 1001)
list_num1 = list(list_num1)
summ = 0
good_set = set()

for n1 in list_num1:
    for n2 in list_num1:
        summ = int(n1) + int(n2)
        summ = str(summ)
        last_digit = int(summ[-1])
        if last_digit == 5:
            summ = int(summ)
            good_set.add(summ)



print(sorted(good_set))