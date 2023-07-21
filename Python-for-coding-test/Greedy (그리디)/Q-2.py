# todo: 가장 큰 수 출력
# 입력 받기
# 무조건 곱셈 연산 (단, 0, 1이 아니라면!)
n = input()
result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
