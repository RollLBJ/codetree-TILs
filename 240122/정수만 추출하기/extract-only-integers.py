a,b = input().split()
num=[]
for i, chr in enumerate(a):
    if chr.isnumeric():
        num.append(chr[:i])
        break

for i, chr in enumerate(b):
    if chr.isnumeric():
        num.append(chr[:i])
        break

print(int(num[0]) + int(num[1]))