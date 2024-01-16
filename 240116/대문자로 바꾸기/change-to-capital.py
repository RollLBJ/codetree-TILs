n=5
def up(t):
    return t.upper()
t = [tuple(map(up,input().split())) for _ in range(5)]

for i in t:
    for j in i:
        print(j,end=" ")
    print('')