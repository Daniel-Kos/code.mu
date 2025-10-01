str_num = "1230450678090"
pos1 = str_num.find('0')

if pos1 != -1:
    pos2 = str_num.find('0', pos1 + 1)
    if pos2 != -1:
        pos3 = str_num.find('0', pos2 + 1)
        if pos3 != -1:
            print(f"Position three zero: {pos3}")