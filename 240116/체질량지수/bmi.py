h,w = map(int,input().split())
h*=0.01
bmi = w/(h*h)
print(int(bmi))
if bmi>=25:
    print("Obesity")