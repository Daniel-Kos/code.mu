data = '2025-12-31'
index = 0
my_tuple = ()
temp_list = list(my_tuple)

for w in data.split('-'):
    if index == 0:
        index += 1
        temp_list.append(w)
    elif index == 1:
        index += 1
        temp_list.append(w)
    elif index == 2:
        temp_list.append(w)

temp_list.reverse()
my_tuple = tuple(temp_list)
print(my_tuple)
