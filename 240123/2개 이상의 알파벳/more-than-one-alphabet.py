a=input()
cnt = []
for i in a:
    if i not in cnt:
        
        cnt.append(i)
    else:
        print('Yes')
        break
else:
    print('No')