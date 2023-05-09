# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    sub_seq = []

    for i in range(len(t) - len(p) + 1):
        sub_seq.append(t[i:i + len(p)])

    for j in sub_seq:
        if j <= p:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution("3141592", "271"))
    print(solution("500220839878", "7"))
