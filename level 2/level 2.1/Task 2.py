num_str = 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10
num = 0
for i in num_str:
    if num == i:
        print(num_str.index(i))
        break