import sys

input = sys.stdin.readline

gears = list(list(input().rstrip()) for _ in range(4))

current_state = []

for gear in gears:
    current_state.append([2, 6])

k = int(input())
options = list(list(map(int,input().split())) for _ in range(k))

def circulate(dir: bool, index: int) -> None:
    visited[index] = True
    left = gears[index][current_state[index][1]]
    right = gears[index][current_state[index][0]]
    if index + 1 < 4 and right != gears[index+1][current_state[index+1][1]] and not visited[index + 1]:
        circulate(not dir, index+1)
    if index -1 >= 0 and left != gears[index-1][current_state[index-1][0]] and not visited[index - 1]:
        circulate(not dir, index-1)

    if dir: # 시계 방향
        current_state[index][0] -= 1
        current_state[index][1] -= 1
    else: # 반시계 방향
        current_state[index][0] += 1
        current_state[index][1] += 1

    current_state[index][0] %= 8
    current_state[index][1] %= 8

for index,direction in options: # 1은 시계, -1은 반시계
    visited = [False for _ in range(4)]
    if direction == 1:
        circulate(True, index-1)
    else:
        circulate(False, index-1)


answer = 0
values = [[1,0],[2,0],[4,0],[8,0]]
for i in range(4):
    rood_id = current_state[i][0] - 2
    if gears[i][rood_id] == "1":
        answer += values[i][0]
print(answer)