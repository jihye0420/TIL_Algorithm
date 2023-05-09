# https://school.programmers.co.kr/learn/courses/30/lessons/120913
def solution(my_str: str, n: int) -> list:
    answer = []
    # my_str = list(my_str)
    while my_str:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer


if __name__ == '__main__':
    print(solution("abc1Addfggg4556b", 6))  # 1
