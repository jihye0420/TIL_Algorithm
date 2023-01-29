# todo: 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/120921
# def solution(A, B):
#     answer = 0
#     a = list(A)
#     count = 0
#     while len(A) <= count:
#         temp_a = a[-1]
#         for i in range(len(a) - 1, -1, -1):
#             print(i)
#             if i == 0:
#                 a[i] = temp_a
#             else:
#                 a[i] = a[i - 1]
#         answer += 1
#         count += 1
#         if a == B:
#             break
#     return answer

# todo: 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/120921
def solution(A: str, B: str) -> int:
    result = 0

    while result != len(A):
        if A == B:
            return result
        A = A[-1] + A[:-1]
        result += 1

    return -1

# if __name__ == '__main__':
#     print(solution("hello", "ohell"))  # 1
#     print(solution("apple", "elppa"))  # -1
