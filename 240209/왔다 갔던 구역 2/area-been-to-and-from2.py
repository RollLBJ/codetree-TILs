N = int(input())
A = [list(map(lambda x: x if x.isalpha() else int(x), input().split())) for _ in range(N)]

result = [0]*2000

index = 1000
result[index] = 1

for cmd in A:
  result[index] += 1
  for _ in range(cmd[0]):
    if cmd[1] == 'R':
      index += 1
    elif cmd[1] == 'L':
      index -= 1
    result[index] += 1

cnt=0
_flag = False
# print(result)
for i in result:
  # if i>=1:
    # print(i, end=' ')
  
  if i>=2:
    cnt+=1
    _flag = True
  if i<=1 and _flag==True:
    cnt-=1
    _flag = False
  
  

print(cnt)