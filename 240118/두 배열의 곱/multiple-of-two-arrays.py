a = [list(map(int,input().split())) for _ in range(3)]
_t=input()
b = [list(map(int,input().split())) for _ in range(3)]


for i in range(3):
    for j in range(3):
        print(f"{a[i][j]*b[i][j]}", end=' ')
    print("")