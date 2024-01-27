n = int(input())
a = list(map(int, input().split()))

a_asc = list(sorted(a))
a_desc = list(sorted(a, reverse=True))

print(' '.join(map(str, a_asc)))
print(' '.join(map(str, a_desc)))