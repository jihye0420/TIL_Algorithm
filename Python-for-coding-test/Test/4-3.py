# n X m 맵 생성
n, m = map(int, input().split())
# 2차원 배열 선언
d = [[0] * m for _ in range(n)]
# 위치, 방향언
x, y, direction = map(int, input().split())
d[x][y] = 1
print(d)

# 전체 맵 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
print(array)

# 북 동 남 서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 회전
def translate():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
# 시뮬레이션 시작
while True:
    # 왼쪽 방향 회전
    translate()
    # 한 칸 전진
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x = nx
        y = ny
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우 => 갈 길이 없다면 왼쪽 방향으로 회전
    else:
        turn_time += 1
    # 모든 방향이 갈 수 없으면!
    if turn_time == 4:
        # 방향 유지 & 한 칸 뒤로 가기
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
