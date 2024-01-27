n, k, t = input().split()
n = int(n)
k = int(k)
arr = [input() for _ in range(n)]
fitered_arr = []
for str in arr:
    if str.startswith(t):
        fitered_arr.append(str)

fitered_arr.sort()
print(fitered_arr[k-1])