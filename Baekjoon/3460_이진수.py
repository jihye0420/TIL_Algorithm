"""
나의 풀이 => todo: 수정해야함
"""
# https://www.acmicpc.net/problem/3460
# def solution(t, data):
#     answer = []
#     for i in range(len(data)):
#         while data[i] >= 1:
#             answer.append(data[i] % 2)
#             data[i] = data[i] // 2
#         for j in range(len(answer)):
#             if answer[j] == 1:
#                 print(j, end=' ')
#         # print()
#         # answer = []
#
#
# if __name__ == '__main__':
#     t = int(input())
#     data = []  # n
#     if t == 1:
#         data.append(int(input()))
#         solution(t, data)
#     else:
#         for _ in range(2):
#             data.append(int(input()))
#             solution(t, data)

"""
다른 풀이
"""
# T = int(input())
#
# for _ in range(T):
#     n = bin(int(input()))[2:]
#     for i in range(len(n)):
#         if n[-i - 1] == '1':
#             print(i, end=" ")

for _ in range(int(input())):
    n = int(input())
    i = 0
    while n > 0:
        if n % 2 == 1:
            print(i, end=' ')
        n = n // 2
        i += 1
