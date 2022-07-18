from collections import defaultdict, deque
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

graph = defaultdict(list)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

possible = deque(combinations((i for i in range(1,n+1)), 2))

answer = [0,0,float("inf")]

while possible:
    a,b = possible.popleft()
    visited = [False for _ in range(n+1)]
    visited[a] = True
    visited[b] = True
    A = deque()
    B = deque()
    cnt = 0
    for i in graph[a]:
        if not visited[i]:
            A.append((i,1))
            visited[i] = True
            cnt += 2
    for i in graph[b]:
        if not visited[i]:
            B.append((i,1))
            visited[i] = True
            cnt += 2
    while A or B:
        tempA = deque()
        tempB = deque()
        while A:
            node, weight = A.popleft()
            for n_node in graph[node]:
                if not visited[n_node]:
                    visited[n_node] = True
                    cnt += (weight + 1) * 2
                    tempA.append((n_node, weight + 1))
        while B:
            node, weight = B.popleft()
            for n_node in graph[node]:
                if not visited[n_node]:
                    visited[n_node] = True
                    cnt += (weight + 1) * 2
                    tempB.append((n_node, weight + 1))
        A = tempA
        B = tempB
    if cnt < answer[2]:
        answer = [a,b,cnt]

for i in answer:
    print(i, end=" ")

# def bfs(i):
#     visited = [0 for _ in range(n+1)]
#     q = deque()
#     q.append((i,0))
#     visited[i] = 1
#     while q:
#         node, weight = q.popleft()
#         for n_node in graph[node]:
#             if not visited[n_node]:
#                 visited[n_node] = weight + 1
#                 q.append((n_node, weight + 1))
#     visited[i] = 0
#     return visited

# def min_sum(a,b):
#     answer = 0
#     for i in range(1,n+1):
#         answer += min(a[i], b[i])
#     return answer

# bfss = []
# for i in range(1,n+1):
#     bfss.append(bfs(i))

# answer = [0,0,float("inf")]
# for i in range(len(bfss)):
#     for j in range(i+1, len(bfss)):
#         temp = min_sum(bfss[i], bfss[j])
#         if temp < answer[2]:
#             answer = [i,j,temp]

# answer[0] += 1
# answer[1] += 1
# answer[2] *= 2
# print(*answer)