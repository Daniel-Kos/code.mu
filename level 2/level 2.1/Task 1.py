success = 0
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
    if n != search_element:
        word_list.remove(n)
    else:
        print(n)

print(word_list)