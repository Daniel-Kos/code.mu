str_num = '12,34,56'
total = 0

for num in str_num.split(','):
    num = int(num)
    total = total + num

print(total)