# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = 0
    numbers = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # dict 메소드 확인해보기, enumerate, items
    for key, value in numbers.items():
        # print(numbers.items())
        # print(key + '' + str(value))
        if key in s:
            s = s.replace(key, str(value))

    # for k in numbers.keys():
    #     print(numbers.keys())
    #     print(k)
    answer = int(s)
    return answer


if __name__ == '__main__':
    print(solution('one4seveneight'))
