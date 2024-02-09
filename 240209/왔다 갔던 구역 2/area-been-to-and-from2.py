N = int(input())
A = [list(map(lambda x: x if x.isalpha() else int(x), input().split())) for _ in range(N)]

result = [0]*2000

index = 1000
# result[index] = 1
for cmd in A:
  if cmd[1] == 'R':
    for i in range(cmd[0]):
      result[index] += 1
      index += 1
  elif cmd[1] == 'L':
    for i in range(cmd[0]):
      result[index] += 1
      index -= 1
cnt=0
_flag = False
# print(result)
for i in result:
  # if i>=1:/
    # print(i, end=' ')
  if i>=2:
    cnt+=1
  

print(cnt)