a = input()
b = input()

res_a = []
res_b = []
for i in a:
    if i.isalpha():
        pass
    else:
        res_a.append(i)

for i in b:
    if i.isalpha():
        pass
    else:
        res_b.append(i)

res_a = int(''.join(res_a))
res_b = int(''.join(res_b))
print(res_a + res_b)