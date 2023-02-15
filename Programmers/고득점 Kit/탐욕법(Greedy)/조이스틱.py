# todo : 다시 풀어보기
# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3

#! 내가 쓴 코드
def solution(name):
    answer = 0
    i = name[0]
    for l in range(0, len(name)):
        tmp = ord(name[l])
        if l == 0:
            a = tmp - 65
            z = 90 - tmp
            if a > z:  # Z에서 더 가까울 때
                answer += 1
                answer += z
            else:  # A에서 더 가까울 때
                answer += 1
                answer += a
        else:
            left = abs(ord(name[l-1]) - tmp)
            right = abs(tmp - ord(name[l-1]))
            if left > right: #오른쪽에 더 가까울 떄
                answer += right
            else: # 왼쪽에 더 가까울 때
                answer += left
    answer += len(name)
    return answer

# def solution(name):
#     change = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
#     print(change)
#     idx, answer = 0, 0
#
#     while True:
#         answer += change[idx]
#         change[idx] = 0
#
#         if sum(change) == 0:
#             break
#
#         left, right = 1, 1
#         print(change[idx])
#         while change[idx - left] == 0:
#             left += 1
#
#         while change[idx + right] == 0:
#             right += 1
#
#         answer += left if left < right else right
#         idx += -left if left < right else right
#
#     return answer


if __name__ == '__main__':
    print(solution("JEROEN"))
    print(solution("JAN"))
