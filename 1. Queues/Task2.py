len_inp = int(input())
inp = input().split()
cash = {int(i) : -1 for i in inp}
max_depth = 0
for i in range(len_inp):
    j = i
    counter = 1
    while inp[int(j)] != '-1':
        if cash[int(inp[int(j)])] > -1:
          #  print('here')
            counter += cash[int(inp[int(j)])]
            break
        counter += 1
        j = inp[int(j)]
    if max_depth < counter : max_depth = counter
    cash[i] = counter
print(max_depth)