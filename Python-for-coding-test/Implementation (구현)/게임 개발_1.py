n, m = map(int, input().split())  # 가로, 세로

x, y, direction = map(int, input().split())  # x, y, 방향

# 0으로 초기화
mymap = [[0] * m for _ in range(n)]
print(mymap)

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
print(array)

# 현재 위치는 방문 처리
mymap[x][y] = 1

# 북 동 남 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽 방향 부터 차례대로 갈 곳을 정하기
# 가보지 않은 칸이 없다면 회전 후 갈 곳 정하기
# 4 방향 모두 가본 칸 or 바다 or 한 칸 뒤 갈 곳 정하기
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if array[nx][ny] == 0 and mymap[nx][ny] == 0:
        mymap[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 존재하지 않는 경우 이동 => 회전만 하기
    else:
        turn_time += 1
    # 4 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
