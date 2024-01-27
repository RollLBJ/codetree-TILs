def recur(n):
    if n==0:
        return
    print("* "*n)
    recur(n-1)
    print("* "*n)

recur(int(input()))