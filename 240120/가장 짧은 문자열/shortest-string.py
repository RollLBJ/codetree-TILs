arr = [ input() for _ in range(3)]

min=21
max=0
for i in range(3):
    if min > len(arr[i]):
        min = len(arr[i])
    if max < len(arr[i]):
        max = len(arr[i])

print(max-min)