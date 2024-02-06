a, b = map(int,input().split())
n = int(input())

res = 0
m=1
while(True):
  if n//10 == 0:
    res += n * m
    break
  else:
    res += n%10 * m
    n = n//10
    m *= a
# print(res)
ans = []
while(True):
  if res//b==0:
    ans.append(res)
    break
  else:
    ans.append(res%b)
    res = res//b

_flag = False

for i in ans[::-1]:
  print(i,end='')