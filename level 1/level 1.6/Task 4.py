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
    if n < 0:
        summ += 0
    else:
        summ += n
print(summ)