a, b = map(int,input().split())
n = int(input())

res = 0
while(True):
  if n//10 == 0:
    res += n * a
    break
  else:
    res += n%10 * a
    n = n//10
    a *= a

ans = []
while(True):
  if res//b==0:
    ans.append(res)
    break
  else:
    ans.append(res%b)
    res = res//b

_flag = False
for i in ans:
  if i != 0:
    _flag = True
  if _flag:
    print(i,end='')