# todo: 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import Counter


def solution(want, number, discount):
    answer = 0
    check = {}
    # zip 함수: 길이가 같은 리스트 등의 요소를 묶어주는 함수
    for w, n in zip(want, number):
        check[w] = n
    print(check)

    # Counter
    for i in range(len(discount) - 9):  # 0~4까지 5번 반복
        c = Counter(discount[i:i + 10])
        print(c)
        if c == check:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
                   ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                    "banana", "apple", "banana"]))
