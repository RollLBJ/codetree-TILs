h,w = map(int,input().split())
w*=0.01
bmi = w//(h*h)
print(int(bmi))
if bmi>=25:
    print("Obesity")