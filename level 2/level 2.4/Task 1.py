s = input("Введите строку: ")
for i, e in enumerate(s):
   if e.isdigit():
      print(i)
      break