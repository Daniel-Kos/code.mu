number_list = []
merged = []
summ = 0


while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)
if len(number_list) % 2 == 1:
        print("There must be an even number of numbers, only numbers that have a pair will be displayed.")


for i in range(0, len(number_list)- 1, 2):
    number1 = str(number_list[i])
    number2 = str(number_list[i + 1])
    summ = number1 + number2
    summ = int(summ)
    merged.append(summ)

print(merged)