# https://school.programmers.co.kr/learn/courses/30/lessons/120912
def solution(array):
    answer = 0
    for i in array:
        # print(i)
        # 7이 있는지 판단하는 기준
        i = str(i)
        for j in range(len(i)):
            if '7' in i[j]:
                answer += 1
    return answer


if __name__ == '__main__':
    print(solution(array=[7, 77, 17]))