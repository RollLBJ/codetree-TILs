a=input()
cnt = []
b_cnt=0
for i in a:
    if i not in cnt:
        cnt.append(i)
    else:
        if b_cnt==2: 
            print('Yes')
            break
        b_cnt+=1
else:
    print('No')