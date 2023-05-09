# todo: 다시 풀어보기
def solution(orders):
    answer = []
    temp_dict = {}

    for i in orders:
        temp = i.split(' ')
        for j in range(len(temp)):
            if j == 0 and temp[j] not in list(temp_dict.keys()):
                temp_dict[temp[j]] = set()
            elif j == 0 and temp[j] in list(temp_dict.keys()):
                continue
            else:
                temp_dict[temp[0]].add(temp[j])
    # print(temp_dict)

    for key, value in temp_dict.items():
        temp_dict[key] = len(value)
    print(temp_dict)

    # value = list(temp_dict.values())
    # max = value[0]
    # for i in range(1, len(value)):
    #     if value[i] >= max:
    #         max = value[i]
    #
    # for k, v in temp_dict.items():
    #     if v == max:
    #         answer.append(k)
    # answer.append(max_value)
    return answer


# from collections import Counter
# from functools import reduce
#
# def solution(orders):
#     answer = []
#     temp_dict = {}
#     for i in orders:
#         if i[0] in temp_dict:
#             temp_dict[i[0]]
#
#     # 1. 의상 종류별 Counter를 만든다.
#     counter = Counter([who for type, who in orders])
#     print(counter)
#
#     # 2. 모든 종류의 count + 1을 누적하여 곱해준다
#     # answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
#     return answer


if __name__ == '__main__':
    print(solution(["alex pizza pasta", "alex pizza pizza", "alex noodle", "bob pasta", "bob noodle sandwich pasta",
                    "bob steak noodle"]))
    print(solution(["alex pizza pasta steak", "bob noodle sandwich pasta", "choi pizza sandwich pizza", "alex pizza pasta steak"]))