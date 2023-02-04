# https://school.programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i < 0:
            break
        else:
            budget -= i
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution([1, 3, 2, 5, 4], 9))
    print(solution([2, 2, 3, 3], 10))

# d = [1, 3, 2, 5, 4]
# for i in d:
#     print(i)
