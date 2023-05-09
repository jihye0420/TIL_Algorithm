# https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for i in commands:
        a, b, k = i[0], i[1], i[2]
        # print(a, b, k)
        # print(array[a - 1:b])
        temp = array[a - 1:b]
        temp.sort()
        # print(temp)
        answer.append(temp[k - 1])
    return answer


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
