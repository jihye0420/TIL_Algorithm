# https://www.acmicpc.net/problem/1541
# * 실버 2
"""
* 아이디어
- '-'가 나오기 전까지 수를 묶어주기
* 알게된 점
"""
data = input()
tmp = data.split('-')
answer = 0
for w, i in enumerate(tmp):
    if '+' in i:
        t = sum(list(map(int, i.split('+'))))
        if w != 0:
            answer -= int(t)
        else:
            answer += int(t)
    elif w == 0:
        answer += int(i)
    else:
        answer -= int(i)
print(answer)
