def short_find(i):
    if i != parent[i]:
        parent[i] = short_find(parent[i])
    return parent[i]

def union(dest, src):

    dest_id = short_find(dest)
    src_id = short_find(src)
    if dest_id == src_id:
        return
    parent[src_id] = dest_id


if __name__ == '__main__':
    n, e, d = [int(i) for i in input().split()]
    parent = [i for i in range(n+1)]
    for i in range(e):
        cmd = [int(i) for i in input().split()]
        union(cmd[0], cmd[1])
    ans = 1
    for i in range(d):
        cmd = [int(i) for i in input().split()]
        if parent[cmd[0]] != parent[cmd[1]]:
            continue
        else:
            ans = 0
            break
    print(ans)
