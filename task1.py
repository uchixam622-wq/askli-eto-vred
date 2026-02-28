with open('input1.txt', 'r') as fin, open('output1.txt', 'w') as fout:
    for line in fin:
        m = int(line.strip())
        if m in (12, 1, 2): res = "Winter"
        elif m in (3, 4, 5): res = "Spring"
        elif m in (6, 7, 8): res = "Summer"
        elif m in (9, 10, 11): res = "Autumn"
        else: res = "Error"
        fout.write(res + '\n')