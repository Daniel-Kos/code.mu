data = '2025-12-31'
dict_total = {}
number = 0

for d in data.split('-'):
    if number == 0:
        dict_total['year'] = int(d)
        number += 1
    elif number == 1:
        dict_total['month'] = int(d)
        number += 1
    elif number == 2:
        dict_total['day'] = int(d)

print(dict_total)