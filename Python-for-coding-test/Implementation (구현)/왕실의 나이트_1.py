yx = input()

map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

# 현재 위치
y = map[yx[0]]
x = int(yx[1])

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, 2, -2, 2, -2]

tmp_x = x
tmp_y = y
result = 0
for xx, yy in zip(dx, dy):
    tmp_x = x + xx
    tmp_y = y + yy
    if tmp_x < 1 or tmp_y < 1 or tmp_x > 8 or tmp_y > 8:
        continue
    result += 1
print(result)
