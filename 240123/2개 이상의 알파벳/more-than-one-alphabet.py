a=input()
cnt = []
b_cnt=0
for i in a:
    if i not in cnt:
        cnt.append(i)
    else:
        print('Yes')
        if b_cnt==1: break
        b_cnt+=1
else:
    print('No')