number_list = []

number = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
}

dict_list = list(number.values())
number_list.extend(dict_list)

print(number_list)