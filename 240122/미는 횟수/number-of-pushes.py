a = input()
b = input()


def shift_right(input_string):
    return input_string[-1] + input_string[:-1]


cnt = 0
while (True):
    if a == b:
        break
    elif cnt >= len(a):
        cnt = -1
        break
    else:
        a = shift_right(a)
    
        cnt += 1

print(cnt if cnt<=len(a) else len(a)-cnt)