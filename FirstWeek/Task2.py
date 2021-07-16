inp = "9 7 5 5 2 9 9 9 2 -1".split()
len_inp = len(inp)
for i in range(len_inp):
    inp[i] = int(inp[i])

leaves = []
for i in range(len_inp):
    if i not in inp:
        leaves.append(i)

def depth(kid: int, base: list):
    if kid == -1:
        return 1
    return 1 + depth(base[kid], base)
max = 0
for i in leaves:
    a = depth(i, inp)
    if a > max:
        max = a
print(max - 1)
'''import sys

sys.setrecursionlimit(2000)
for i in range(len(inp)):
    inp[i] = int(inp[i])
tree_kids = {}
root = inp.index(-1)
for i in range(len(inp)):
    if inp[i] not in tree_kids:
        tree_kids[inp[i]] = []
    else:
        continue
    for j in range(len(inp)):
        if inp[j] == inp[i]:
            tree_kids[inp[i]].append(j)
cash = [-1 for i in range(len(inp))]

# print(cash)
def height(root, h = 1):
  #  print(cash[root])
    if cash[root] > -1:
        return cash[root]
    if root in tree_kids:
        for i in tree_kids[root]:
            cash[i] = h
            h = max(h, 1 + height(i))
    cash[root] = h
    return h


print(height(root) - 1)
print(cash)'''