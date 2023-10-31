"""
백트래킹 코드는 대략 아래와 같은 포맷
"""


def backtrack(candidate):
    # 만약 현재 후보군이 유효한 해라면 정답 처리하고 backtrack 함수를 종료
    if find_solution(candidate):
        output(candidate)
        return

    # 반복문을 돌면서 가능한 모든 후보군에 대해 탐색
    for next_candidate in list_of_candidates:
        # 유효한 후보군인 경우에만 탐색 진행
        if is_valid(next_candidate):
            # 이 후보군을 우선 추가하고,
            place(next_candidate)
            # 후보군을 추가한 상태에서 다음 후보군에 대해서 탐색 진행
            backtrack(next_candidate)
            # 해당 후보군에 대한 탐색을 종료한 이후에는 제거
            remove(next_candidate)


