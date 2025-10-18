def patten(n, d):
    if n==0:
        return
    if d!=n+1:
        print("*"*d)
        patten(n, d+1)

n = int(input("Enter value of n: "))
patten(n, 1)