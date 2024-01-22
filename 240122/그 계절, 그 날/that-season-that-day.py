def is_yoon(year):
    if year%4 ==0 and year%100==0 and year%400:
        return True
    elif year%4==0 and year%100==0:
        return False
    elif year%4==0:
        return True



y,m,d = map(int,input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
if is_yoon(y):
    month[1]=29

if m>=1 and m<=12:
    if d>=1 and d<=month[m-1]:
        if month in [3, 4, 5]:
            print("Spring")
        elif month in [6, 7, 8]:
            print("Summer")
        elif month in [9, 10, 11]:
            print("Fall")
        else:
            print("Winter")