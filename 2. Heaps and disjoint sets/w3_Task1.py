def short_find(i):
    if i != parent[i]:
        parent[i] = short_find(parent[i])
    return parent[i]

def findParent(i):
    while i != parent[i]:
        i = parent[i]
    return i



def union(dest, src):
    global m_rank
    dest_id = short_find(dest)
    src_id = short_find(src)

    if dest_id == src_id:
        ans.append(m_rank)
        return
    parent[src_id] = dest_id
    rank[dest_id] += rank[src_id]
    if rank[dest_id] > m_rank:
        m_rank = rank[dest_id]
    ans.append(m_rank)


if __name__ == '__main__':
    n, m = [int(i) for i in input().split()]
    rank = [int(i) for i in input().split()]
    parent = [i for i in range(n+1)]
    rank.insert(0,0)
    m_rank = max(rank)
    ans = []
    for i in range(m):
        cmd = [int(i) for i in input().split()]
        union(cmd[0], cmd[1])
    for i in ans:
        print(i)



