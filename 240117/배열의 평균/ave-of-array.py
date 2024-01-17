t = [list(map(int,input().split())) for _ in range(2)]

total=0
for i in t:
    print(sum(i)/4, end=" ")
    total+=sum(i)

print()
for i in range(len(t[0])):
    print((t[0][i]+t[1][i])/2, end=" ")
print()
print(total/8)