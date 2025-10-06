word = 'aaa bbb ccc eee fff'
word_2 = []
index = 0

for i in word.split( ):
    if index % 2 == 0:
        index += 1
        word_2.append(i)
    elif index % 2 == 1:
        index += 1
        word_v2 = i[:1].upper() + i[1:]
        word_2.append(word_v2)
print(word_2)
