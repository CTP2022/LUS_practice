# 팰린드롭인지 확인

# for 문을 활용한 단순 비교
strs = []
for char in input:
	if char.isalnum():
		strs.append(char.lower())

while len(strs):
	if strs.pop(0) != strs.pop():
		print("False")
		break
else:
	print("True")

# deque를 사용한 최적화
from collections import deque

strs = deque()
for char in input:
	if char.isalnum():
		strs.append(char.lower())

while len(strs):
	if strs.popleft() != strs.pop():
		print("False")

# 정규 표현식
import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]