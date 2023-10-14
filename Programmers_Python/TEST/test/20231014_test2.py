# def solution(products, purchased):
#     answer = ''
#     # products => dict {"p": ["",""]}
#     # purchased => list []
#     # value 들 만의 개수를 세기 => 등장회수가 높은 값들을 더하기
#     # 구매 안한 값들만 뽑기
#
#     # products 의 key, value를 구함
#     result_dict = {}
#     for item in products:
#         elements = item.split()
#         key = elements[0]
#         value = elements[1:]
#         if key in result_dict:
#             result_dict[key].append(value)
#         else:
#             result_dict[key] = value
#     print(result_dict)
#
#     # 등장 개수를 셈
#     count_dict = {}
#     for values in result_dict.values():
#         for value in values:
#             count_dict[value] = count_dict.get(value, 0) + 1
#     print(count_dict)
#     return answer

def solution(products, purchased):
    pref = {}  # {"특성": 개수}
    products = [p.split() for p in products]  # 공백을 기준으로 나누기
    # print(products)
    products_dic = {p[0]: p[1:] for p in products}  # 공백을 기준으로 key, value로 구성
    # print(products_dic)

    # 고객이 구매한 적 있는 제품의 특성 개수 세기
    for i in products:
        if i[0] in purchased:
            for p in i[1:]:
                if pref.get(p):
                    pref[p] += 1
                else:
                    pref[p] = 1
    # print(pref)

    pref = sorted(sorted([[i, pref[i]] for i in pref]), key=lambda x: x[1], reverse=True)  # 개수가 많은 것으로 정렬
    # print(pref)

    rec_lst = sorted(list(set([i[0] for i in products]) - set(purchased)))  # 구매하지 않은 제품
    # print("rec_lst:", rec_lst)

    rec_lst_tmp = rec_lst[:]  # 복사
    # print(rec_lst_tmp)

    for i in pref:  # 선호 특성
        for j in rec_lst_tmp:  # 구매하지 않은 제품 리스트
            if i[0] not in products_dic[j]:
                print("i[0]: ", i[0])
                rec_lst_tmp.remove(j)
                print(rec_lst_tmp, rec_lst)
        # 필요한 조건문인지 판단해보기!
        if len(rec_lst_tmp) == 0:
            rec_lst_tmp = rec_lst
        elif len(rec_lst_tmp) == 1:
            return rec_lst_tmp[0]


if __name__ == '__main__':
    print(solution(["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"],
                   ["towel", "mattress", "curtain"]))
    print(solution(
        ["towel red long thin", "blanket red thick short", "curtain red long wide", "mattress thick", "hat red thin",
         "pillow red long", "muffler blue thick long"], ["blanket", "curtain", "hat", "muffler"]))
