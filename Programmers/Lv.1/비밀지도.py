# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    array = [[0] * n for _ in range(n)]  # 반드시 이렇게 초기화해야함!
    # 2진수로 만들기 arr1의 list값 & arr2의 list값
    print(array)
    for j in range(n):
        temp = [0] * n
        for i in range(n):
            temp[i] = arr1[j] % 2
            arr1[j] = arr1[j] // 2
        temp.reverse()
        array[j] = temp
    # print(array)

    for j in range(n):
        temp = [0] * n
        for i in range(n):
            temp[i] = arr2[j] % 2
            arr2[j] = arr2[j] // 2
        temp.reverse()
        # array[j] = temp
        for k in range(n):
            if array[j][k] == 0 and temp[k] == 1:
                array[j][k] = 1
    # print(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 1:
                array[i][j] = '#'
            else:
                array[i][j] = ' '
        answer.append(''.join(array[i]))
    # print(array)
    return answer


if __name__ == '__main__':
    print(solution(5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28]))

# # 2진수 만들기
# test = 9
# n = 5
# temp = [0] * 5
# for i in range(n):
#     temp[i] = test % 2
#     test = test // 2
# temp.reverse()
# print(temp)
