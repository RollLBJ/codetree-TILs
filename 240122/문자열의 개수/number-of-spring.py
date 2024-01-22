cnt=0
arr = []
 while(True):
    _temp = input()
    if _temp == 0:
        break
    else:
        cnt+=1
        if cnt%2==1:
            arr.append(_temp)
print(cnt)
for i in arr:
    print(i)