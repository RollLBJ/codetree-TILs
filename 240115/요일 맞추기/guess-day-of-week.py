m = [31,28,31,30,31,30,31,31,30,31,30,31]
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

m1, d1, m2, d2 = map(int,input().split())

if m2>m1:
    total_day=m[m1-1]-d1+d2
    for i in range(m1+1,m2):
        total_day+=m[i]
elif m1>m2:
    total_day=m[m2-1]-d2+d1
    for i in range(m2+1,m1):
        total_day+=m[i]
else:
    total_day=d2-d1
        

# print(total_day)
print(weekday[-(abs(total_day)%7)])