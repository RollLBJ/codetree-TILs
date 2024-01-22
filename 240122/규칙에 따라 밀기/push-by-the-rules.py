str = input()
cmds = input()

for cmd in cmds:
    if cmd=='L':
        str = str[1:]+str[0]
    elif cmd=='R':
        str = str[-1]+str[:-1]
print(str)