def solution(books, target):
    answer = 0
    for i in target:
        for idx, val in enumerate(books):
            if i == val:
                answer += idx
                books.remove(val)  # 값을 삭제
                books.insert(0, val)  # 0 번째 인덱스에 값을 넣기
                break
    return answer


if __name__ == '__main__':
    print(solution([3, 1, 2], [1, 3, 2]))
    print(solution([1, 2, 3, 4], [4, 4, 3, 2, 1]))
