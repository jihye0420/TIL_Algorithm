"""
# 실행 시 아래 에러 발생
# => 재귀의 최대 깊이를 초과했다는 내용
# => 파이썬 인터프리터는 호출 횟수 제한이 있는데 이 한계를 벗어남
# => 무한대로 재귀 호출을 진행 할 수 없다.
# * RecursionError: maximum recursion depth exceeded while calling a Python object
"""
# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
#
# recursive_function()

"""
# * 재귀 함수 스택의 자료구조를 이용 & 종료 조건 필요
"""


# * 팩토리얼 구현
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:  # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)


# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
