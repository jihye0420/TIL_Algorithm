# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    s = s.split(' ')
    temp = []
    for i in s:
        temp.append(i.capitalize())  # capitalize() : 첫번째 글자만 대문자로 바꿔줌
    print(temp)
    answer = " ".join(temp)
    return answer


if __name__ == '__main__':
    print(solution("3people unFollowed me"))
    print(solution("for the last week"))

# def solution(s):
#     # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     s = s.split(' ')
#     temp = []
#     for i in s:
#         temp.append(i.capitalize())
#         count = 0
#         # i = list(i)
#         # for j in i:
#         #     if j in numbers:
#         #         continue
#         #     else:
#         #         print("???")
#         #         print(j.upper())
#         #         j = j.upper()
#         #         count += 1
#         #     if count == 1:
#         #         break
#         # i = ''.join(i)
#     answer = ' '.join(temp)
#     return answer
