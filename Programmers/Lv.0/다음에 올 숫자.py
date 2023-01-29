def solution(common):
    answer = 0
    a1 = common[1] - common[0]
    a2 = common[2] - common[1]
    if a1 == a2:
        answer = common[-1] + a1
    else:
        answer = common[-1] * (common[1] // common[0])
    return answer
