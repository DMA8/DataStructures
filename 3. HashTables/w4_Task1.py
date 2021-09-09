n_cmd = int(input())
phonebook = {}
ans = []
for i in range(n_cmd):
    cmd = input().split()
    if cmd[0] == 'add':
        phonebook[cmd[1]] = cmd[2]
    elif cmd[0] == "find":
        if cmd[1] in phonebook:
            ans.append(phonebook[cmd[1]])
        else:
            ans.append('not found')
    elif cmd[0] == 'del':
        phonebook.pop(cmd[1], None)
for i in ans:
    print(i)