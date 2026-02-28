with open('input3.txt', 'r') as fin, open('output3.txt', 'w') as fout:
    for line in fin:
        w, h, r = map(int, line.split())
        res = "YES" if (r * 2 <= w and r * 2 <= h) else "NO"
        fout.write(res + '\n')
        