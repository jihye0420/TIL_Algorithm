# https://www.acmicpc.net/problem/1316
# * 실버 5
"""
* 아이디어
- 문자가 바뀌는 시점을 확인
* 알게된 점
- 문자열 슬라이스
"""
n = int(input())
group_words = []
for i in range(n):
    data = input()
    group_words.append(data)
    for j in range(len(data) - 1):
        if data[j] == data[j + 1]:
            continue
        elif data[j] in data[j + 1:]:
            group_words.remove(data)
            break
print(len(group_words))
