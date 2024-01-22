n1, n2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for num1,i in enumerate(arr1):
    if i==arr2[0]:
        is_continuous = False
        for num2,j in enumerate(arr2):
            if arr1[num1+num2]==j:
                pass
            else:
                break
        else:
            is_continuous = True
            print("Yes")
            break
else:
    print("No")