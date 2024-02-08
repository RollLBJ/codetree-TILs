N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(K)]
result = [0] * N
for cmd in A:
  for i in range(cmd[0], cmd[1]+1):
    result[i] += 1

print(max(result))