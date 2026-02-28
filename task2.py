with open('input2.txt', 'r') as fin, open('output2.txt', 'w') as fout:
    for line in fin:
        c, h, o = map(int, line.split())
        res = min(c // 2, h // 6, o)
        fout.write(str(res) + '\n')
        