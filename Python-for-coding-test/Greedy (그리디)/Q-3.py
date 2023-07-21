# todo: 문자열 뒤집기 -> 연속 숫자만 가능
# 0,1 문자열 S
# 뒤집어서 최소 횟수로 숫자 통일!

number = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번쨰 원소 확인
if number[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(number) - 1):
    if number[i] != number[i + 1]:
        if number[i + 1] == '0':
            count1 += 1  # 1로 바꾸기
        else:
            count0 += 1  # 0로 바꾸기
print(min(count0, count1))  # 바꾸는 최솟값 출력
