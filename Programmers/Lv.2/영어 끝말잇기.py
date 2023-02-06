# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    temp = []
    tmp = 0

    for i in words:
        tmp += 1
        if temp:
            if i in temp:
                break
            if temp[-1][-1] != i[0]:
                break
        temp.append(i)
    # print(tmp)
    answer.append(tmp // n)
    return answer


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    # print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
    #                    "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
