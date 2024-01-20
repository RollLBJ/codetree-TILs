a = input()
cnt=0
res=[]
for char in a:
    cnt+=1
    if cnt%2==0:
        res.append(char)

print(''.join(reversed(res)))