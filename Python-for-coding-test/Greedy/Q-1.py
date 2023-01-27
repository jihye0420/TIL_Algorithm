# N : 모험가 수
# a, b, ... : 모험가 공포도

# todo: 그룹수의 최댓값
n = input()
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도 낮은 사람순으로
    count += 1  # 현재 그룹에 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면!
        result += 1  # 그룹 결성
        count = 0  # 현재 그룹 초기화
print(result)
