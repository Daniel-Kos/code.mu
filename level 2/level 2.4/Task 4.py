word = 'abcde'
index_word = 0
result_list = []

for i in word:
    if index_word % 2 == 0:
        index_word += 1
        i = i.upper()
        result_list.append(i)
    else:
        index_word += 1
        result_list.append(i)

result_str = ''.join(result_list)
print(result_str)