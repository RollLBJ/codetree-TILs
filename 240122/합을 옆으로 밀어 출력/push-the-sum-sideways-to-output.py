n = int(input())
arr = [int(input()) for _ in range(n)]
total = str(sum(arr))
total = total[1:] + total[0]
print(total)