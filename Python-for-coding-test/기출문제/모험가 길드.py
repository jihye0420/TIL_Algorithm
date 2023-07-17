n = map(int, input())
data = list(map(int, input().split()))

# for i in range(n):
#     data.append(map(int, input().split()))

data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
