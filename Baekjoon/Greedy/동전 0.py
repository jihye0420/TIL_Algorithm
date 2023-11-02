n, k = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))

count = 0
while k >= 0 and data:
    j = data.pop()

    if k >= j:
        count += k // j
        k = k % j

    else:
        continue
print(count)
