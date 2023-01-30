# todo: 다른 사람 풀이 참고해보기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s: list):
    answer = []
    zero_cnt = 0
    count = 0
    while s != '1':
        # if '0' in s:
        #     s = s.replace('0', '')
        #     zero_cnt += 1
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        len_s = len(s)
        # bin() 정수를 이진수로 변환 => 0b로 시작!
        s = bin(len_s)[2:]
        # print(s)
        count += 1
    answer.append(count)
    answer.append(zero_cnt)
    return answer


if __name__ == '__main__':
    print(solution("110010101001"))
    print(solution("01110"))
