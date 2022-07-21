import heapq
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
T = [int(input()) for _ in range(n)]

heap = []

for i in range(len(T)):
    heapq.heappush(heap, [T[i], i])

passed = 0

while heap:
    cur, index = heapq.heappop(heap)
    now = cur + T[index]
    heapq.heappush(heap, [now, index])
    passed += 1
    if passed == m:
        print(cur)
        break


# 🤦‍♂️ heap 자체에 길이 N만큼 저장되어 있고, 
# m의 크기를 맞추기 위해 M번 while문이 도는 과정에서 시간초과가 날 수 밖에 없음 -> 입력값이 크니까 이진 탐색 🤦‍♂️

import sys

input = sys.stdin.readline

n,m = map(int,input().split())
T = [int(input()) for _ in range(n)]
left = min(T)
right = max(T)*m
answer = right

while left <= right:
    total = 0
    mid = (left + right) // 2
    for t in T:
        total += mid // t
    if total >= m:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1
print(answer)