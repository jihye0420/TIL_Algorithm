# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
from typing import List


# ! 내가 쓴 풀이 => 테스트 케이스는 모두 통과
# ! 정확성: 54.2
# ! 효율성: 0.0
# ! 합계: 54.2 / 100.0
# def solution(phone_book: List[str]) -> bool:
#     answer = True
#     temp = phone_book
#     # 리스트의 하나씩 요소를 꺼내서 비교
#     for idx, phone in enumerate(phone_book):
#         phone_book.pop(idx)
#         for j in phone_book:
#             if phone in j:
#                 answer = False
#                 break
#         phone_book = temp
#     return answer

# ! 아래와 같이 문제를 단순화 하는 것이 중요함 !!!
def solution(phone_book):
    answer = True

    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break

    return answer


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12","123","1235","567","88"]))
