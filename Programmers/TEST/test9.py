def solution(fees, usage):
    answer = 0
    tmp = 0 # idx 저장
    # 기본료
    for i in range(0, len(fees)):
        if i != len(fees) - 1:
            if fees[i][0] < usage <= fees[i + 1][0]:
                answer += fees[i + 1][1]
                tmp = i + 1
        elif i == len(fees) - 1:
            if fees[i - 1][0] < usage:
                answer += fees[i][1]
                tmp = i
    # 그 이후 요금 계산
    if tmp != 0:
        for i in range(0, tmp): # 0,1
            if i == 0:
                answer += fees[i][0] * fees[i][2]
            else:
                answer += (fees[i][0] - fees[i - 1][0]) * fees[i][2]
        usage -= fees[tmp - 1][0]
        if usage != 0:
            answer += usage * fees[tmp][2]
    elif tmp == 0:
        answer += fees[tmp][1]
        answer += usage * fees[tmp][2]
    return answer


if __name__ == '__main__':
    print(solution([[200, 910, 93], [400, 1600, 188], [655, 7300, 281], [0, 15372, 435]], 320))
    print(solution([[200, 910, 93], [400, 1600, 188], [655, 7300, 281], [0, 15372, 435]], 450))
    print(solution([[1851, 1000, 100], [0, 2000, 155]], 1205))
    print(solution([[100, 415, 90], [250, 1600, 389], [0, 7000, 480]], 530))
