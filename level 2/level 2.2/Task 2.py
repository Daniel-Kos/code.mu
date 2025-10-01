number_list = []
positive_list = []
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
    if i > 0:
        positive_list.append(i)
    else:
        pass

print(positive_list)