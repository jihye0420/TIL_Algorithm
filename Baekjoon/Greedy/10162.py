timer = int(input())
array = [300, 60, 10]
count = []
tmp = 0
for a in array:
    tmp = timer // a
    timer = timer % a
    count.append(tmp)

if timer != 0:
    print(-1)
else:
    for i in count:
        print(i, end=' ')
