number_list = []
negative_list = []
summ = 0

while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)

for i in number_list:
    i = int(i)
    if i < 0:
        negative_list.append(i)
    else:
        pass

negative = len(negative_list)

print(negative)