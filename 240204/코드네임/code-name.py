class member:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score


members = [member() for _ in range(5)]

minscore = 101
minscore_index = -1
for i in range(5):
    codename, score = input().split()
    members[i].codename = codename
    members[i].score = score
    if score<minscore:
        minscore = score
        minscore_index = i


print(members[i].codename, members[i].score)