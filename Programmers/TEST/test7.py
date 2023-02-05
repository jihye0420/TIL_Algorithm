def HistogramArea(arr):
  areas = []
  for i in range(1,len(arr)+1 ):
    for j in range(i):
      h = min(arr[j:i])
      w = i - j
      areas.append(h*w)
  # code goes here
  return max(areas)


# keep this function call here
print(HistogramArea([6, 3, 1, 4, 12, 4]))