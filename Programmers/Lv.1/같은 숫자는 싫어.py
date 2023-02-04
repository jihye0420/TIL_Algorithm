# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    temp = arr[0]
    tmp = 0
    answer.append(temp)
    for i in range(1, len(arr)):
        if temp == arr[i]:
            tmp += 1
            temp = arr[i]
        else:
            tmp = 0
            temp = arr[i]
            answer.append(arr[i])
    return answer


if __name__ == '__main__':
    print(solution([1, 1, 3, 3, 0, 1, 1]))
