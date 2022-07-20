import sys

input = sys.stdin.readline

n,m = map(int,input().split())

game = list(list(map(int,input().split())) for _ in range(n))

pSum = [[0 for _ in range(m+1)] for _ in range(n+1)]
for r in range(1,n+1):
    for c in range(1,m+1):
        pSum[r][c] = pSum[r-1][c] + pSum[r][c-1] - pSum[r-1][c-1] + game[r-1][c-1]

answer = -100000

for r1 in range(1,n+1):
    for c1 in range(1,m+1):
        for r2 in range(r1, n+1):
            for c2 in range(c1, m+1):
                answer = max(answer, pSum[r2][c2] - pSum[r2][c1-1] - pSum[r1-1][c2] + pSum[r1-1][c1-1])

print(answer)