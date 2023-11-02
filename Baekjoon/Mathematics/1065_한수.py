# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수
# 한수: 양의 정수 X의 각 자리가 등차수열

n = int(input())


# 각 자리의 수가 등차수열인지 확인
def check(n):
    tmp = 0
    for num in range(1, n + 1):
        # 100 보다 작으면 -> 등차수열
        num = str(num)
        if int(num) < 100:
            tmp += 1
        # 100 같거나 큰 수이고 1000보다 작은 경우 -> 세자리 수 (차)
        elif int(num[1]) - int(num[0]) == int(num[2]) - int(num[1]):
            tmp += 1
    return tmp


print(check(n))
