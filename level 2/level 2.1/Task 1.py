word_list = []
deli_word = []
search_element = "https://"

while True:
    word = input("Enter a link: ")
    if word == "exit":
        break
    else:
        word_list.append(word)

for n in word_list:
    if "https://" in n:
        deli_word.append(n)

print(deli_word)

