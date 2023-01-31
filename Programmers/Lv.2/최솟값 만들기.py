# ! 효율성 테스트 확인해보기 => 테스트 케이스에는 다 맞음
# 채점 결과
# 정확성: 69.6
# 효율성: 0.0
# 합계: 69.6 / 100.0
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    for i in range(len(A)):
        max_value_a = max(A)
        max_value_b = max(B)
        min_value_a = min(A)
        min_value_b = min(B)
        if (max_value_a * min_value_b) > (max_value_b * min_value_a):
            # print('1')
            A.remove(min_value_a)
            B.remove(max_value_b)
            answer += max_value_b * min_value_a
        else:
            # print('2')
            A.remove(max_value_a)
            B.remove(min_value_b)
            answer += max_value_a * min_value_b
        # print(answer)
    return answer


if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 4]))
    print(solution([1, 2], [3, 4]))
