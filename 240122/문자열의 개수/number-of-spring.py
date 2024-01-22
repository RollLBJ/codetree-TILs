cnt=0
arr = []
while(True):
    try:
        temp = input()
        if temp == '0':
            break
        else:
            cnt+=1
            if cnt%2==1:
                arr.append(temp)
    except:
        pass
print(cnt)
for i in arr:
    print(i)