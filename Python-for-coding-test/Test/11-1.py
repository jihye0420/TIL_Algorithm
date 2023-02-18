# 모험가 길드
n = map(int, input().split())
array = list(map(int, input().split()))
array.sort()
result = 0  # 총 그룹의 수
count = 0  # 현재 그룹의 모험가 수
# 현재 공포도를 확인
# 현재 공포도와 그룹 수가 같거나 크면 그룹 결성 그만하기
for a in array:
    count += 1
    if count >= a:
        result += 1
        count = 0
print(result)
