# * 완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
# * 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 직접 수행
n = int(input())
x, y = 1, 1
plans = input().split()
print(plans)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
