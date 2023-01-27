# todo: 문자열 뒤집기
# 0,1 문자열 S
# 뒤집어서 최소 횟수로 숫자 통일!

number = input()
count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

if number[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(number) - 1):
    # if number[i] != number[i + 1]: