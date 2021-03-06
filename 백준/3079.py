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


# ๐คฆโโ๏ธ heap ์์ฒด์ ๊ธธ์ด N๋งํผ ์ ์ฅ๋์ด ์๊ณ , 
# m์ ํฌ๊ธฐ๋ฅผ ๋ง์ถ๊ธฐ ์ํด M๋ฒ while๋ฌธ์ด ๋๋ ๊ณผ์ ์์ ์๊ฐ์ด๊ณผ๊ฐ ๋  ์ ๋ฐ์ ์์ -> ์๋ ฅ๊ฐ์ด ํฌ๋๊น ์ด์ง ํ์ ๐คฆโโ๏ธ

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