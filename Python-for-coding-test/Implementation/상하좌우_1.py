n = int(input())

plan = list(input().split())

# 현재 위치
x, y = 1, 1

# U D R L
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 이동 후 위치 파악을 위한 변수
temp_x, temp_y = 1, 1

for i in plan:
    if i == 'U':
        temp_x = x + dx[0]
        temp_y = y + dy[0]
    elif i == 'D':
        temp_x = x + dx[1]
        temp_y = y + dy[1]
    elif i == 'R':
        temp_x = x + dx[2]
        temp_y = y + dy[2]
    elif i == 'L':
        temp_x = x + dx[3]
        temp_y = y + dy[3]
    if temp_x < 1 or temp_y < 1 or temp_x > n or temp_y > n:
        continue
    x = temp_x
    y = temp_y

print(x, y)
