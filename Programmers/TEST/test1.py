def solution(p, m, d):
    answer = -1
    r = 0.01
    if p == d:
        return 0
    while True:
        temp = p * (1 + r) ** m
        if d <= temp:
            break
        r += 0.01
    return round(r * 100)


if __name__ == '__main__':
    print(solution(10000000, 9, 13000000))
    print(solution(1000000, 3, 1000000))
