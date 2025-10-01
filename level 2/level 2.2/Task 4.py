word_list = []
deli_word = []
search_element = ".html"

while True:
    word = input("Enter a file full name: ")
    if word == "exit":
        break
    else:
        word_list.append(word)

for n in word_list:
    if ".html" in n:
        deli_word.append(n)

print(deli_word)