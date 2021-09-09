m = int(input())
n = int(input())
table = [[] for _ in range(m)]
ans = []


def hsh(word:str)->int:
    hsh = 0
    for letter in range(len(word)):
        hsh += ord(word[letter]) * pow(263, letter)
        hsh %= 1000000007
    return hsh % m


for i in range(n):
    cmd = input().split()
    h = hsh(cmd[1])
    if cmd[0] == "add":
        if cmd[1] not in table[h]:
            table[h].insert(0, cmd[1])
    elif cmd[0] == "check":
        print(*table[int(cmd[1])])
    elif cmd[0] == "find":
        if cmd[1] in table[h]:
            print('yes')
        else:
            print('no')
    elif cmd[0] == "del":
        if cmd[1] in table[h]:
            table[h].remove(cmd[1])




