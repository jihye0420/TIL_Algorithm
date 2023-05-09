# https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=python3
# todo: 다시 풀어보기
# from itertools import combinations

# ! 모든 테스트 케이스에 만족하지 않음 & combinations 사용법
# def solution(number, k):
    # pick_count = len(number) - k
    # return ''.join(sorted(list(combinations(number, pick_count)), reverse=True)[0])

def solution(number, k):
    stack = []
    for n in number:
        # stack의 값이 존재하고, k가 0보다 크며, stack의 맨 위 값이 현재의 n보다 작으면
        while stack and stack[-1] < n and k > 0:
            # stack의 맨 위 값을 제거하고 k도 -1 해준다.
            stack.pop()
            k -= 1
        # 현재의 n값은 무조건적으로 stack에 넣어준다.
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    # ex) 일반적으로 k는 0일텐데 ex) k = 3 number = 1000000 이런 경우엔 k는 처음 인풋받은 그대로 유지됨
    # 이럴 때 답은 뒷 숫자를 k개만큼 없애준 1000 이므로 슬라이싱을 stack[:-k]로 해주는 것
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


if __name__ == '__main__':
    print(solution("1924", 2))
    print(solution("1231234", 3))
