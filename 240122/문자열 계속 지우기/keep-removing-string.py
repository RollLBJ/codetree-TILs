a = input()
b = input()

while(True):
    for i in range(len(a)):
        if a[i]==b[0]:
            for j in range(len(b)):
                _diff = 0
                if (i+j) < len(a):
                    if a[i+j] != b[j]:
                        # print('다름')
                        _diff=1
                else:
                    _diff=1
            if _diff==0:
                # print('발견')
                a = a[:i] + a[i+len(b):]
                break
    
    if _diff==1:
        break
print(a)