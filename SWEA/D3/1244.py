tc = int(input())
for c in range(1, tc + 1):
    number = list(map(int, input().split()))
    numbers = list(map(int, str(number[0])))
    m = number[1]
    temp = []
    for i in range(m + 1):
        max_num = max(numbers)
        numbers.remove(max_num)
        temp.append(max_num)
    print(f"#{c}", int(''.join(list(map(str, temp)) + list(map(str, numbers)))))
