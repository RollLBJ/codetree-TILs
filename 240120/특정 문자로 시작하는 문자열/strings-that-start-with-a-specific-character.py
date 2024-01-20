n = int(input())
a = [input() for _ in range(n)]
char = input()

total = 0
cnt = 0
for i in a:
    if i.startswith(char):
        total += len(i)
        cnt += 1

print("{} {:.2f}".format(cnt,total / cnt if cnt > 0 else 0))