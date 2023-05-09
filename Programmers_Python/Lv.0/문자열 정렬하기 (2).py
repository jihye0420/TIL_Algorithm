# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    answer = ''.join(sorted(my_string))
    return answer


if __name__ == '__main__':
    print(solution("Bcad"))
    print(solution("heLLo"))
