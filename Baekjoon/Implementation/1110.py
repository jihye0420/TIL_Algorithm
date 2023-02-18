def solution(number):
    if number == '0':
        return '1'
    count = []
    if len(number) == 1:
        number = '0' + number
    tmp = int(number[0]) + int(number[1])
    tmp = str(tmp)
    if len(tmp) == 1:
        tmp = '0' + tmp
    tmp = number[-1] + tmp[-1]
    count.append(tmp)

    while True:
        tmp = int(count[-1][0]) + int(count[-1][1])
        tmp = str(tmp)
        tmp = count[-1][-1] + tmp[-1]
        if len(tmp) == 1:
            tmp = '0' + tmp
        count.append(tmp)
        if number == tmp:
            break
    return len(count)


if __name__ == '__main__':
    number = input()
    print(solution(number))
