n = int(input())  # 설탕

cnt = 0  # 봉지수
while n >= 0:  # 설탕이 남아있으면
    if n % 5 == 0:  # 5의 배수일때
        cnt += n // 5
        print(cnt)
        break
    n -= 3  # 5의 배수가 될때까지 3킬로 봉지에 담기
    cnt += 1
else:
    print(-1)  # 설탕이 0이 아니라 음수가 될 경우 5,3키로로 나눌 수 없음을 의미
