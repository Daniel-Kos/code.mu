number_list = []
fractions_list = []
summ = 0

while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)

for i in number_list:
    i = float(i)
    i = round(i, 1)
    fractions_list.append(i)

print(fractions_list)