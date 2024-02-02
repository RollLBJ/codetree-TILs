class test():
    def __init__(self, id_num='codetree', level=10):
        self.id_num = id_num
        self.level = level
a,b = input().split()

t1 = test()
print(f"user {t1.id_num} lv {t1.level}")
t1.id_num = a
t1.level= b
print(f"user {t1.id_num} lv {t1.level}")