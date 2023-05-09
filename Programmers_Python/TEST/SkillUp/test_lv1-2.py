# https://programmers.co.kr/skill_checks/462907?challenge_id=15802
def solution(food: list):
    answer = ''
    # 리스트 선언
    # 각 개수 /2로 들어갈 수 있는 개수 정하기!
    count = 0
    for i in food:
        count += i
    count -= 1  # 0번쨰 물 제외
    count = count // 2
    eat = [] * count

    for j in range(1, len(food)):
        tmp = food[j] // 2
        for t in range(tmp):
            eat.append(j)
    reversed_eat = reversed(eat)
    answer = ''.join(list(map(str, eat))) + '0' + ''.join(list(map(str, reversed_eat)))
    return answer


if __name__ == '__main__':
    print(solution([1, 3, 4, 6]))
