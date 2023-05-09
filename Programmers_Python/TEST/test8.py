def LongestConsecutive(arr):
    arr.sort()
    temp = arr[0]
    answer = []
    tmp = []
    for i in range(len(arr)):
        temp += 1
        if temp == arr[i]:
            answer.append(temp)
        else:
            tmp.append(len(answer))
            answer = []
            temp = arr[i]
            print(arr[i])
    if answer:
        tmp.append(len(answer))
    return max(tmp) + 1


# keep this function call here
# print(LongestConsecutive([4, 3, 8, 1, 2, 6, 100, 9]))
print(LongestConsecutive([5, 6, 1, 2, 8, 9, 7]))
