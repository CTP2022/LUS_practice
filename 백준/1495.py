import sys

input = sys.stdin.readline

n,s,m = map(int,input().split())

num_set = set()
num_set.add(s)

volumes = list(map(int,input().split()))

for volume in volumes:
    temp_set = set()
    while num_set:
        num = num_set.pop()
        if num - volume >= 0:
            temp_set.add(num - volume)
        if num + volume <= m:
            temp_set.add(num + volume)
    num_set = temp_set

print(max(num_set) if num_set else -1)

