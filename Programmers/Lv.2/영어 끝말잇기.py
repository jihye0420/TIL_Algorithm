# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    temp = []
    temp.append(words[0])
    number, order = 0, 0
    for i in range(1, len(words)):
        if words[i] in temp or temp[-1][-1] != words[i][0]:
            number = (i % n) + 1
            order = (i // n) + 1
            break
        temp.append(words[i])
    return [number, order]


if __name__ == '__main__':
    print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
    print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                       "hang", "gather", "refer", "reference", "estimate", "executive"]))
    print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
