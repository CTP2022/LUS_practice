import sys
input = sys.stdin.readline

pan = list(list(input().rstrip()) for _ in range(8))
domino = [[False]*7 for _ in range(7)]
visited = [[False]*7 for _ in range(8)]
# 방향은 좌 상단 -> 우 하단
dr = [1,0] # 아래측 확인
dc = [0,1] # 우측 확인

def backTracking(r,c):
    if r == 8: # 다 맞춰진것 -> 1 리턴
        return 1
    nr, nc = r, c + 1 # 다음 좌표
    if nc == 7:
        nr, nc = r + 1, 0
    if visited[r][c]: # 이미 도미노가 놓인 곳이라면
        return backTracking(nr,nc)

    count = 0
    dom1 = int(pan[r][c])
    visited[r][c] = True
    for i in range(2):
        x,y = r + dr[i], c + dc[i]
        if 0 <= x < 8 and 0 <= y < 7:
            dom2 = int(pan[x][y])
            if not visited[x][y] and not domino[dom1][dom2]:
                domino[dom1][dom2] = True
                domino[dom2][dom1] = True
                visited[x][y] = True
                count += backTracking(nr,nc)
                domino[dom1][dom2] = False
                domino[dom2][dom1] = False
                visited[x][y] = False

    visited[r][c] = False
    return count

print(backTracking(0,0))