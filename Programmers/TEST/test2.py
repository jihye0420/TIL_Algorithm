def solution(waiting):
    answer = []
    # for i in waiting:
    #     if i not in answer:
    #         answer.append(i)
    #     else:
    #         continue
    # [answer.append(x) for x in waiting if x not in answer]
    answer=list(dict.fromkeys(waiting))
    return answer


if __name__ == '__main__':
    print(solution([1, 5, 8, 2, 10, 5, 4, 6, 4, 8]))

