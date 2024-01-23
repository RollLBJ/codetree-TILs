a=input()
cnt = []
for i in a:
    if i not in cnt:
        print(cnt)
        cnt.append(i)
    else:
        print('Yes')
        break
else:
    print('No')