# todo: 다시 풀어보기

# 좌, 우측 숫자의 개수는 num이 짝수이냐 홀수이냐에 따라 다르기 때문에
# 왼쪽 끝 값을 구하기 위해서는 num - 1로 하고 우측은 num + 2를 하면 짝수, 홀수를 구분하지 않고 연속적인 리스트를 구할 수 있다
def solution(num, total):
    average = total // num
    return [i for i in range(average - (num - 1) // 2, average + (num + 2) // 2)]
