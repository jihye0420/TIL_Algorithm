# https://school.programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    category = {}

    # 같은 종류의 옷끼리 묶어서 사전에 저장
    for i in clothes:
        if i[1] in category.keys():
            category[i[1]].append(i[0])
        else:
            category[i[1]] = [i[0]]

    # 경우의 수 구하기 : 각 종류별로 옷을 0개 또는 1개를 입음! => 각 종류별로 입을 수 있는 옷의 개수에 안 입는 경우 1을 더하고 그 값들을 모두 곱하기
    for value in category.values():
        answer *= len(value) + 1
    # 아무것도 안 입는 경우 1가지는 빼기
    return answer - 1


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
