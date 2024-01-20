arr = [ input() for _ in range(2)]

for i in arr:
    for j in i.split():
        print(j, end='')