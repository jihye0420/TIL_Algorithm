# https://school.programmers.co.kr/learn/courses/30/lessons/120849
def solution(my_string: str):
    answer = ''
    aeiou = ['a', 'e', 'i', 'o', 'u']
    my_string = list(my_string)
    for i in range(len(my_string)):
        if my_string[i] in aeiou:
            my_string[i] = ''
    answer = ''.join(my_string)
    return answer


if __name__ == '__main__':
    print(solution('bus'))
