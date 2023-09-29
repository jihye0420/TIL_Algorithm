n = int(input())
data = list(map(int, input().split()))
# 정렬
data.sort()

# 현재 공포도가 그룹을 형성한 값보다 크거나 같다면!
count = 0  # 현재 그룹 구성원 수
current = data[0]  # 현재 공포도
answer = 0

for i in data:
    count += 1
    if count >= i:
        count = 0
        answer += 1

print(answer)
