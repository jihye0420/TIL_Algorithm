# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number: str):
    answer = ''
    answer = "*" * len(phone_number[:-4]) + phone_number[-4:]
    return answer


if __name__ == '__main__':
    print(solution("01033334444"))
