h,w = map(int,input().split())
w*=0.01
bmi = w/(h*h)
if bmi>=25:
    print("Obesity")