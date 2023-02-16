# https://programmers.co.kr/skill_checks/462956?challenge_id=536
from typing import List


def solution(dirs: str) -> int:
    answer = 0
    dx = [0, 0, -1, 1]  # U,D,L,R
    dy = [1, -1, 0, 0]  # U,D,L,R
    ways = ['U', 'D', 'L', 'R']
    dirs: List[str] = list(dirs)
    x, y = 0, 0
    temp = []

    for d in dirs:
        idx = [idx for idx, v in enumerate(ways) if v == d]
        if -6 >= x + dx[idx[0]] or x + dx[idx[0]] >= 6 or -6 >= y + dy[idx[0]] or y + dy[idx[0]] >= 6:
            continue
        x = x + dx[idx[0]]
        y = y + dy[idx[0]]
        if (x, y) not in temp or (x, y) != temp[-1]:
            temp.append((x, y))
    print(temp)
    answer = len(temp)
    return answer


if __name__ == '__main__':
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
