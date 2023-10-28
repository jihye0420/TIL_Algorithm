# https://www.acmicpc.net/problem/4673
# * 실버 5
"""
* 아이디어
- set
* 알게된 점
- for문으로 리스트, 집합 선언
"""

"""
* set에서 사용할 수 있는 함수
"""
numbers = set(range(1, 10000))
remove_set = set()  # 생성자가 있는 숫자 set
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)  # add: 집합에 요소를 추가할 때

self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
for self_num in sorted(self_numbers):  # sorted 함수로 정렬
    print(self_num)
