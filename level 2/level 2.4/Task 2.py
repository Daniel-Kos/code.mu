num = input()
positive_num = 0

for i in num:
    i = int(i)
    if i % 2 == 0:
        positive_num += 1

print(positive_num)