# * 리스트
# 크기가 N, 모든 값이 0인 1차원 리스트
n = 10
data = [0] * n
print(data)

# 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, '10']
print(a)
print(a[-1])
print(a[-3])
print(a[2:5])
print(a[2:])
print(a[:4])

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
print(array)
# 2차원 배열 선언
n = 3
m = 4
array = [[0] * m for _ in range(n)]  # 반드시 이렇게 초기화해야함!
# array = [[0] * m] * n  # 이렇게 초기화 시, 의도하지 않은 결과 나옴
print(array)

# 리스트 관련 메서드
b = [2, 3, 4]
b.append(7)  # 원소 끝에 삽입
print(b)
b.insert(1, 3)  # 인덱스, 원소 값
print(b)
b.sort()  # 정렬, 오름차순
print(b)
# b.sorted()  # 정렬, 새로운 리스트 반환
# print(b)
b.pop()  # 원소 빼기
print(b)
b.reverse()  # 역순 정렬
print(b)
c = b.count(3)  # 특정 값 가지는 데이터 개수
print(c)
b.remove(3)  # 특정 값 가지는 원소 제거
print(b)

# * 주요 라이브러리 문법 & 유의점
# 표준 라이브러리: 특정 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리
# 6가지
# 1. 내장함수: print(), input() 기본 입출력 기능, sorted() 정렬기능 등 필수 기능 제공
# 2. itertools: 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리, 순열&조합 라이브러리 제공
# 3. heapq: 힙(Heap) 기능을 제공하는 라이브러리, 우선순위 큐 기능을 구현하기 위해 사용
# 4. bisect: 이진탐색(Binary Search) 기능을 제공하는 라이브러리
# 5. collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함하고 있는 라이브러리
# 6. math: 필수적인 수학적 기능 제공하는 라이브러리, 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 pi와 같은 상수 포함

# * 내장함수
# input(), print(), sum(), min(), max(), eval(), sorted()

# * itertools
# class: permutations, combinations
# permutations : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)계산