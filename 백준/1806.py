from collections import deque
import sys

input = sys.stdin.readline

n,s = map(int,input().split())
nums = list(map(int,input().split()))

if s in nums:
    print(1)
    exit()

sub_nums = deque()
total = 0
answer = float("inf")

for num in nums:
    sub_nums.append(num)
    total += num
    if total > s:
        while total > s:
            answer = min(answer, len(sub_nums))
            poped_num = sub_nums.popleft()
            total -= poped_num
    if total == s:
        answer = min(answer, len(sub_nums))

print(answer if answer != float("inf") else 0)
