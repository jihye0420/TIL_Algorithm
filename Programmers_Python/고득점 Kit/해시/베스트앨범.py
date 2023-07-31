# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# def solution(genres: list, plays: list) -> list:
#     answer = []
#     dict_category = {}  # { 카테고리 : [재생횟수]}
#     total = {}  # { 카테고리 : 총합}
#     dict_song = dict(zip(genres, plays))
#     for i in zip(genres, plays):
#         if i[0] in dict_category.keys():
#             dict_category[i[0]].append(i[1])
#             total[i[0]] += i[1]
#         else:
#             dict_category[i[0]] = [i[1]]
#             total[i[0]] = i[1]
#
#     total = sorted(total.items(), key=lambda x: x[1], reverse=True)
#     print(total)
#
#     for k, v in dict_category.items():
#         dict_category[k] = sorted(v, reverse=True)
#     print(dict_category)
#
#     for i in total:
#         print(i)
#         print(dict_category[i[0]][0])
#         print(dict_category[i[0]][1])
#         for idx, v in enumerate(plays):
#             if dict_category[i[0]][0] == v:
#                 print(v)
#                 answer.append(idx)
#             elif dict_category[i[0]][1] == v:
#                 print(v)
#                 answer.append(idx)
#
#     # 노래가 많이 재생된 장르 고르기
#     # 장르 내 많이 재생된 노래 수록
#     # 고유 번호 낮은 것 수록
#     return answer

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    print(dic1)
    print(dic2)
    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer


if __name__ == '__main__':
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
