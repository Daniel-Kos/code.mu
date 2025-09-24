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
    if 0 < n <= 10:
        summ += n
    else:
        summ += 0
print(summ)