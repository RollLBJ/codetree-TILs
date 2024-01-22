str, q=input().split()
q=int(q)
for i in range(q):
    cmd=int(input())
    if cmd==1:
        str = str[1:]+str[0]
    elif cmd==2:
        str = str[-1]+str[:-1]
    elif cmd==3:
        str = str[::-1]
    print(str)