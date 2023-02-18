cost = 1000 - int(input())  # 입력받은 잔돈
array = [500, 100, 50, 10, 5, 1]  # 잔돈 종류
answer = 0  # 개수
for a in array:
    answer += cost // a
    cost = cost % a
    if cost == 0:
        break
print(answer)
