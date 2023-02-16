# https://programmers.co.kr/skill_checks/462907
from datetime import date


def solution(a: int, b: int) -> str:
    answer = ''
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    what = date(year=2016, month=a, day=b).weekday()
    answer = days[what]
    return answer


if __name__ == '__main__':
    print(solution(5, 24))
