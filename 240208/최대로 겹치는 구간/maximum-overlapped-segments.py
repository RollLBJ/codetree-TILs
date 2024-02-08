N = int(input())
A = [list(map(lambda x : int(x)+100, input().split())) for _ in range(N)]

result = [0]*200

for cmd in A:
  for i in range(cmd[0], cmd[1]):
    result[i-1] += 1

print(max(result))