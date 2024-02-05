from functools import cmp_to_key
class student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
def comparator(a, b):
    t1 = -int(a.kor) - int(a.eng) - int(a.math)
    t2 = -int(b.kor) - int(b.eng) - int(b.math)
    
    if t1 > t2:
        return -1
    elif t1 < t2:
        return 1
    else:
        return 0


n = int(input())
students = [ student(*input().split()) for _ in range(n) ]
students.sort(key=cmp_to_key(comparator))


for s in students:
    print(s.name, s.kor, s.eng, s.math)