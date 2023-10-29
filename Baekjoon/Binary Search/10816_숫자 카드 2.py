# 입력
# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
"""
나만의 풀이 => 시간초과ㄴ
"""
n = int(input())
data = list(map(int, input().split()))
# data = {}
# data

m = int(input())
check = list(map(int, input().split()))

for i in check:
    print(data.count(i), end=' ')
"""
이분 탐색
"""
n = int(input())
data = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

# while
