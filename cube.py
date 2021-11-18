
def cb(x):
    return x*x*x
    
x = range(20)

for n in x:
    print("x = ", n)
    if n%2 == 0:
        print("output = ", n)
    else:
        print("output = ", cb(n))
