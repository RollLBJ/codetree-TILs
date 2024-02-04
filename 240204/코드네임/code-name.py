class member:
    def __init__(self, codename='none', score=-1):
        self.codename = codename
        self.score = score


members = [member() for _ in range(5)]

minscore = 101
minscore_index = -1
for i in range(5):
    codename, score = input().split()
    score = int(score)
    members[i].codename = codename
    members[i].score = score
    if score<minscore:
        print(score, i)
        minscore = score
        minscore_index = i


print(members[minscore_index].codename, members[minscore_index].score)