class Secret:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

temp = input().split()
Secret1 = Secret(temp[0], temp[1], temp[2])

print("secret code :", Secret1.code)   
print("meeting point :", Secret1.point)   
print("time :", Secret1.time)