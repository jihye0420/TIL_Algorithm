# todo: 확인해보기 => 정답 보기
# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 내가 푼 풀이
# 답은 동일한데 틀림
def solution(s: str):
    s = s.replace('{', '')
    s = s.replace('}', '')
    s = s.split(',')
    s = list(s)
    answer = []
    for i in s:
        if int(i) not in answer:
            answer.append(int(i))
    return answer


# 맞은 정답
def solution(s):
    ls = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)
    result = []
    # print(ls)
    for l in ls:
        for s in l:
            if int(s) not in result:
                result.append(int(s))
                break
    return result


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    print(solution("{{20,111},{111}}"))
    print(solution("{{123}}"))
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
