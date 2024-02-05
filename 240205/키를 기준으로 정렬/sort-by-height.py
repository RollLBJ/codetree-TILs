class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


n = int(input())
students = [student(*input().split()) for _ in range(n)]
students.sort(key=lambda x: (int(x.height)))

for s in students:
    print(s.name, s.height, s.weight)