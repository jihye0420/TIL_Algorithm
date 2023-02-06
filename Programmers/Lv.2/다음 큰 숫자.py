# https://school.programmers.co.kr/learn/courses/30/lessons/12911
def solution(n):
    answer = 0
    temp_n = list(bin(n)[2:])
    count_n = temp_n.count('1')
    print(count_n)
    up_n = n + 1
    while True:
        list_up_n = list(bin(up_n)[2:])
        count_up = list_up_n.count('1')
        if count_up == count_n and up_n > n:
            break
        up_n += 1
    answer = up_n
    return answer


if __name__ == '__main__':
    print(solution(78))
