from collections import deque
import sys

input = sys.stdin.readline
row,col = map(int,input().split())
pictures = list(list(map(int,input().split())) for _ in range(row))
dr = [1,-1,0,0]
dc = [0,0,1,-1]

def find_picture(r,c):
    q = deque()
    q.append([r,c])
    volume = 1
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < row and 0 <= nc < col and pictures[nr][nc]:
                pictures[nr][nc] = 0
                q.append([nr,nc])
                volume += 1
    answer[1] = max(answer[1], volume)

answer = [0,0]

for r in range(row):
    for c in range(col):
        if pictures[r][c] == 1:
            pictures[r][c] = 0
            find_picture(r,c)
            answer[0] += 1

for i in answer:
    print(i)