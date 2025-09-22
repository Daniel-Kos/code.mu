number_list = []
while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)
print(number_list[::2])