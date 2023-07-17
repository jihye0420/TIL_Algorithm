# https://www.acmicpc.net/problem/2504
data = list(input())

stack = []

result = 0
temp = 1

for i in range(len(data)):
    # if i == 0:
    #     if data[i] == ')' or data[i] == ']':
    #         result = 0
    #         break
    if data[i] == '(':
        temp *= 2
        stack.append(data[i])

    elif data[i] == '[':
        temp *= 3
        stack.append(data[i])

    elif data[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if data[i - 1] == '(':
            result += temp
        temp //= 2
        stack.pop()

    elif data[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if data[i - 1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
