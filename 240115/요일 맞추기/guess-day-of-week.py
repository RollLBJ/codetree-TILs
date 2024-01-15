m_total = [31,28,31,30,31,30,31,31,30,31,30,31]
weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']

m1, d1, m2, d2 = map(int,input().split())

daysum=0

if m2>m1:
    daysum = sum(m_total[m1:m2-1])
elif m2<m1:
    daysum = sum(m_total[m2:m1-1])

if d2>d1:
    print(weekday[(daysum+d2-d1)%7])
elif d2<d1:
    print(weekday[-(daysum+d1-d2)%7])