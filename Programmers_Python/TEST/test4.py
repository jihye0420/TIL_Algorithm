# todo: 다시 풀어보기
def solution(card, word):
    answer = []
    temp = [0] * len(card)
    for w in word:
        print(w)
        for c in card:
            if w in c:
                print(c.index(w))
            pass

    return answer


if __name__ == '__main__':
    print(solution(["ABACDEFG", "NOPQRSTU", "HIJKLKMM"], 'GPQM'))
