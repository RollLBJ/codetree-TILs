class number:
    def __init__(self,num,index):
        self.num = num
        self.index = index

n = int(input())
l = list(map(int,input().split()))
numbers = []

for index, num in enumerate(l):
    numbers.append(number(num,index))

numbers = sorted(numbers, key=lambda x : x.num)

result = [0]*n
for new_index, i in enumerate(numbers):
    # print(i.num, i.index)
    result[i.index] = new_index+1

print(*result)