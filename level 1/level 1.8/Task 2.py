number_list = []
interest_list = []
summ = 0

while True:
    num = input()
    if num == "exit":
        sorted(number_list)
        break
    else:
        number_list.append(num)

for n in number_list:
    n = float(n)
    interest_num = n * 0.10
    interest_num = n + interest_num
    interest_list.append(interest_num)

print(interest_list)