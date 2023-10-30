"""
* 내가 푼 풀이 => 답은 맞으나 런타임 에러
"""
# tc = int(input())
# for c in range(1, tc + 1):
#     number = list(map(int, input().split()))
#     numbers = list(map(int, str(number[0])))
#     m = number[1]
#     temp = []
#     for i in range(m + 1):
#         max_num = max(numbers)
#         numbers.remove(max_num)
#         temp.append(max_num)
#     print(f"#{c}", int(''.join(list(map(str, temp)) + list(map(str, numbers)))))
"""
* 다른 풀이
완전탐색 해서 값들을 set에 넣어 중복을 제거하고 가장 큰 값을 찾았다. nxt는 교환시마다 경우의 수들을 넣기 위한 임시공간이다.
now에는 값들을 계속 갱신해준다.
"""
for tc in range(1, int(input()) + 1):
    data, K = input().split()  # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i + 1, N):
                    s[i], s[j] = s[j], s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print('#{} {}'.format(tc, max(map(int, now))))
