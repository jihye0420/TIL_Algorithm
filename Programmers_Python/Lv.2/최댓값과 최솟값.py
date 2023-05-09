# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    temp_list = []
    for i in s.split(' '):
        temp_list.append(int(i))
    # print(answer)
    max_value = max(temp_list)
    min_value = min(temp_list)
    answer = str(min_value) + ' ' + str(max_value)
    return answer


if __name__ == '__main__':
    print(solution("1 2 3 4"))
    print(solution("-1 -2 -3 -4"))
    print(solution("-1 -1"))
