n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

for num, i in enumerate(a):
    i.append(num+1)

new = sorted(a, key=lambda a:(a[0],a[1]))

for row in new:
    print(*row)