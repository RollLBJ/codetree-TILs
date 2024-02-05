class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
students = [ student(*input().split()) for _ in range(n) ]
students.sort(key=lambda x: (-int(x.kor), -int(x.eng), -int(x.math)))
for s in students:
    print(s.name, s.kor, s.eng, s.math)