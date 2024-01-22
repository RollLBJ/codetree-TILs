a = input()
print(a[:1],end='')
for i in a[1:]:
    if a[1] == i:
        print(a[0],end='')
    else:
        print(i,end='')