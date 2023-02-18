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

# 2차원 배열 입력 받기
array = [0, 0, 0, 0, 0]
print('arr1: ', array)
array = [0] * 5
print('arr2: ', array)
array = [i for i in range(2, 9) if i % 2 == 0]
print('arr3: ', array)

brr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('brr1: ', brr)
brr = [[1, 2, 3]] * 3
print('brr2: ', brr)
brr = [[1, 2, 3] for i in range(3)]
print('brr3: ', brr)
brr = [[i, j] for i in range(3) for j in range(4)]
print('brr4: ', brr)

n, m = 2, 3  # map(int, input().split())
# [0] * m => list(map(int, input().split()))
# 1
mylist = [[0] * m for _ in range(n)]
print('mylist1: ', mylist)
# 2
for i in range(n):
    mylist[i] = [0] * m
print('mylist2: ', mylist)

# 3
# mylist = []
# for i in range(n):
#     mylist.append(list(map(int, input().split())))
# print('mylist3: ', mylist)

# 출력
a = [[10, 20], [30, 40], [50, 60]]
# 0
for x, y in a:
    print(x, y)
print('===============================================')
# 1
for i in a:  # a에서 안쪽 리스트를 꺼냄
    for j in i:  # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()
print('===============================================')
# 2
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print('===============================================')
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
# combinations : iterable 객체에서 r개의 데이터를 뽑아 나열하는 모든 경우(조합)계산
# permutations : iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)계산
# from itertools import permutations
# for j in permutations(possible_lang, i):
#     temp_lang.append(''.join(j))

# * json
# json: 데이터를 주고 받는데 사용하는 경량의 데이터 형식
# 인코딩: 파이썬 변수를 JSON 객체로 변환 json.dumps()
# 디코딩: Json 객체를 파이썬의 기본 자료형으로 변환 json.loads()

# * zip, enumerate,
# zip 함수: 길이가 같은 리스트 등의 요소를 묶어주는 함수
# enumerate 함수: 리스트의 idex와 요소를 함께 가져올 수 있는 함수

# * Counter : 중복된 데이터가 저장된 배열을 인자로 넘기면, 각 원소가 몇번씩 나오는지 저장된 객체를 얻음
# from collections import Counter
# Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
# >>> Counter({'hi': 3, 'hey': 2, 'hello': 1})


# * 정규표현식 : 특정한 규칙을 가진 문자열의 패턴을 표현하는데 사용하는 표현식
# 텍스트에서 특정 문자열을 검색하거나, 치환할때 주로 사용
# ex) 전화번호, 이메일 주소 발췌, 로그 파일에서 특정 에러 메시지 들어간 라인들을 찾을 때 사용함
import re

text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group())  # 에러 1033

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = regex.search(text)
phonenumber = matchobj.group()  # 032-232-3245
print(phonenumber)

text = "문의사항이 있으면 032-232-3245 으로 연락주시기 바랍니다."

regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matchobj = regex.search(text)
areaCode = matchobj.group(1)
num = matchobj.group(2)
fullNum = matchobj.group()
print(areaCode, num)  # 032 232-3245


def eat(food):
    answer = ''
    if food == '양고기':
        answer = '죠아!!!'
    elif food == '초밥':
        answer = '죠아!!!'
    elif food == '???':
        answer = '!!!'
    else:
        answer = '만보걷기'
    return answer


if __name__ == '__main__':
    eat('???')
