"""
# * 나의 풀이
"""
# def solution(nums):
#     set_num = set(nums)
#     tmp = len(nums) // 2
#     if tmp > len(set_num):
#         answer = len(set_num)
#     else:
#         answer = tmp
#     return answer

"""
# * 다른 풀이
"""
from collections import Counter


def solution(nums):
    myPocketmonNum = len(nums) // 2

    # countDict = dict(Counter(nums))
    countDict = Counter(nums)

    if (len(countDict) >= myPocketmonNum):
        return myPocketmonNum
    else:
        return len(countDict)


if __name__ == '__main__':
    print(solution([3, 1, 2, 3]))
    print(solution([3, 3, 3, 2, 2, 4]))
    print(solution([3, 3, 3, 2, 2, 2]))
