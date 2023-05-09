# https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums: list) -> int:
    """
    :param nums: 고를 수 있는 폰켓몬 종류 번호의 list
    :return: 가장 많은 종류의 폰켓몬 선택하는 방법, 그때의 종류 번호의 개수 (최대 고를 수 있는 폰켓몬 종류의 수)
    """
    answer = 0
    num = len(nums) // 2  # 가져갈 수 있는 개수
    tmp = set(nums)  # 폰켓몬의 종류 & len함수를 통해 그 개수를 구함

    if num > len(tmp):  # 골라야하는 폰켓몬의 수 > 폰켓몬 종류의 수 => 종류의 수 반환
        answer = len(tmp)
    else:  # 그외에는 골라야 하는 폰켓몬의 수를 반환
        answer = num
    return answer


if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))
