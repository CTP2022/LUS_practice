# 문자열 뒤집는 함수
return input[::-1]
# 슬라이싱 사용
input = ["h","e","l","l","o"]
print(id(input), input)
input = input[::-1]
print(id(input), input)
input[:] = input[::-1]
print(id(input), input)

#result
1555264380416 ['h', 'e', 'l', 'l', 'o']
1555264380544 ['o', 'l', 'l', 'e', 'h']
1555264380544 ['h', 'e', 'l', 'l', 'o']