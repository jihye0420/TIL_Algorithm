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
array = [[0] * m] * n  # 이렇게 초기화 시, 의도하지 않은 결과 나옴
print(array)

# 리스트 관련 메서드
b = [2, 3, 4]
b.append() # 원소 끝에 삽입
b.sort() # 정렬, 오름차순
b.sorted() # 정렬, 새로운 리스트 반환
b.pop() # 원소 빼기
b.reverse() # 역순 정렬
b.count() # 특정 값 가지는 데이터 개수
b.remove() # 특정 값 가지는 원소 제거
