num_list = []
del_num1 = 5

while True:
    num = int(input("Enter a numbers: "))
    if num == -1:
        break
    else:
        num_list.append(num)

for n in num_list:
    if n == del_num1:
        num_list.remove(n)

print(num_list)