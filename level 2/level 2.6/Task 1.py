word = '023m0df0dfg0'
index = 0
list_index = []

for i in word:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        list_index.append(index)
        index += 1
    else:
        index += 1

print(list_index)