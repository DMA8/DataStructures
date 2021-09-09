P = input()
T = input()
x = 263
p = 10000007
#saved_hashes = []

def count_hash(inp: str) -> int:
    hsh = 0
    for i in range(len(inp)):
        hsh += ord(inp[i]) * pow(x, i, p)
    return hsh % p

x_powp = pow(x, len(P) - 1) % p
hash_pattern = count_hash(P)
hash_last_wrd = count_hash(T[len(T) - len(P):])
ans = []


for i in range(len(T) - 1, len(P) - 2, -1):
    #saved_hashes.append(hash_last_wrd)
    if hash_pattern == hash_last_wrd:
        ans.append(i - len(P) + 1)
   # hash_last_wrd = (hash_last_wrd + p) % p
    hash_last_wrd = ((hash_last_wrd - (ord(T[i]) * x_powp)%p)%p * x % p + ord(T[i - len(P)])%p)

for i in range(len(ans)):
    print(ans.pop(), end=' ')