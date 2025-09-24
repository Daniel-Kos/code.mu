number_list = []
summ = 0

while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)

for n in number_list:
    n = int(n)
    summ = summ + (n ** 2)
print(summ)