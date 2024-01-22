a,b = input().split()
ans = []
for num, i in enumerate(a):
    if not(i.isnumeric()):
       ans.append(a[:num])
else:
    ans.append(a)

for num, i in enumerate(b):
    if not(i.isnumeric()):
       ans.append(b[:num])
print(int(ans[0]) + int(ans[1]))