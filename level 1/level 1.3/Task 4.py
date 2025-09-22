number_list = []
while True:
    num = input("Enter a number: ")
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)
counter_num = len(number_list)
print(number_list[counter_num - 4: counter_num - 1])