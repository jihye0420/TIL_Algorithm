# todo: 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

# ! 내가 쓴 풀이
# def solution(s):
#     answer = 0
#     s = list(s)
#     tmp = 0
#     temp = s[0]
#     for i in range(1, len(s)):
#         if temp == s[i]:
#             tmp += 1
#         else:
#             temp = s[i]
#             tmp = 1
#         if tmp == 2:
#             answer = 1
#             break
#     return answer


def solution(s):
    stack = []
    for c in s:

        if len(stack) == 0:
            stack.append(c)
            continue

        if stack[-1] == c:
            stack.pop()

        else:
            stack.append(c)

    if len(stack) == 0:
        return 1

    else:
        return 0


if __name__ == '__main__':
    print(solution("baabaa"))
    print(solution("cdcd"))
