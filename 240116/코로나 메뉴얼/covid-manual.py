a = list(input().split())
b = list(input().split())
c = list(input().split())

cnt=0
for t in [a,b,c]:
    if t[0] == 'Y' and int(t[1])>=37:
        cnt+=1
if cnt>=2:
    print("E")
else:
    print("N")