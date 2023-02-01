# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):  # 0 ~ 5
    for j in range(60):  # 0 ~ 59
        for k in range(60):  # 0 ~ 59
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
