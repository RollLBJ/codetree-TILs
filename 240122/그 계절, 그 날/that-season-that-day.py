def is_yoon(year):
    if year%4 ==0 and year%100==0 and year%400==1:
        return True
    elif year%4==0 and year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False


y,m,d = map(int,input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
if is_yoon(y):
    month[1]=29
print(y,m,d,month)
if d>=1 and d<=month[m-1]:
    if m in [3, 4, 5]:
        print("Spring")
    elif m in [6, 7, 8]:
        print("Summer")
    elif m in [9, 10, 11]:
        print("Fall")
    else:
        print("Winter")
else:
    print(-1)