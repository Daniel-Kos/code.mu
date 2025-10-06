word = str(input())
index_word = 1
result_list = []

for i in word:
    if index_word % 2 == 0:
        i = i.upper()
        index_word += 1
        result_list.append(i)
    else:
        i = i.lower()
        index_word += 1
        result_list.append(i)

result_str = ''.join(result_list)
print(result_str)