n = int(input())

data = list(input().split())

# L R U D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

x = 1
y = 1


def check(tmp_x, tmp_y):
    if tmp_x in [0, n + 1] or tmp_y in [0, n + 1]:
        return False
    return True


for i in data:
    if i == 'L':
        tmp_x = x + dx[0]
        tmp_y = y + dy[0]
    elif i == 'R':
        tmp_x = x + dx[1]
        tmp_y = y + dy[1]
    elif i == 'U':
        tmp_x = x + dx[2]
        tmp_y = y + dy[2]
    elif i == 'D':
        tmp_x = x + dx[3]
        tmp_y = y + dy[3]
    result = check(tmp_x, tmp_y)
    if result:
        x = tmp_x
        y = tmp_y
    else:
        continue
print(x, y)
