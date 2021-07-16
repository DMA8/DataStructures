inp = "9 7 5 5 2 9 9 9 2 -1".split()

len_inp = len(inp)
leaves = []
for i in range(len_inp):
    if str(i) not in inp:
        leaves.append(i)
max_depth = 0
for i in leaves:
    a = i
    c = 0
    while a != '-1':
        a = inp[int(a)]
        c += 1
    if c > max_depth: max_depth = c
print(max_depth)