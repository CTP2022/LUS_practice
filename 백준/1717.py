import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())

parents = [i for i in range(n+1)]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a

def find(a):
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]


for _ in range(m):
    op, a, b = map(int,input().split())
    if a > b:
        a,b = b,a
    if op:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)