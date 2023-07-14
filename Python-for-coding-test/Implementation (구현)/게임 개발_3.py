n, m = map(int, input().split())

x, y, d = map(int, input().split())

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mymap = [[0] * m for _ in range(n)]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


mymap[x][y] = 1

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if array[nx][ny] == 0 and mymap[nx][ny] == 0:
        x = nx
        y = ny
        count += 1
        turn_time = 0
        mymap[nx][ny] = 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
