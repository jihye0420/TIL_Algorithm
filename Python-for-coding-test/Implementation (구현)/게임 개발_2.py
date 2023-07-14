n, m = map(int, input().split())

x, y, dir = map(int, input().split())

mymap = [[0] * m for _ in range(n)]

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mymap[x][y] = 1
result = 1
turn_time = 0


def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


while True:
    # 왼쪽 회전
    turn_left()
    # 방향별 이동할 좌표 값
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 방문하지 않았던 곳이라면 => 방문
    if array[nx][ny] == 0 and mymap[nx][ny] == 0:
        x = nx
        y = ny
        result += 1
        turn_time = 0
        mymap[nx][ny] = 1
        continue
    # 방문했던 곳이라면 => 회전만 수행 후 다시
    else:
        turn_time += 1
    # 4 방향 모두 갈 수 없는 경우 => 아래 조건 후 다시 1단계
    if turn_time == 4:
        # 방향 유지하여 한칸뒤로 이동할 좌표 값
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 갈 수 없다면 움직이지 말기
        else:
            break
        turn_time = 0

print(result)
