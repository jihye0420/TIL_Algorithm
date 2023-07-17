# https://www.acmicpc.net/problem/2501
def solution(n, k):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append(i)
    if 0 <= k - 1 < len(answer):
        return answer[k - 1]
    else:
        return 0


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solution(n, k))

"""
다른 풀이
"""
