word = 'abcdefg'
index_word = 1
result_list = []

for i in word:
    if index_word % 3 == 0:
        index_word += 1
    else:
        index_word += 1
        result_list.append(i)

result_str = ''.join(result_list)
print(result_str)