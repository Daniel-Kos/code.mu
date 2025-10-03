num_list = [1, 2, 3, 4, 5, 6]
index_number = 0
even_numbers = 0
odd_numbers = 0

for n in num_list:
    if index_number % 2 == 0:
        index_number += 1
        even_numbers = even_numbers + n
    elif index_number % 2 == 1:
        index_number += 1
        odd_numbers = odd_numbers + n

print(even_numbers / odd_numbers)