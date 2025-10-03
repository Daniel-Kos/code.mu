word = '023m0df0dfg0'
set_index = set()

for i,x in enumerate(word):
    if x == '0':
        set_index.add(i)
print(set_index)