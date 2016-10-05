def fibonacci(n):
    a=0
    b=1
    c=0
    print (a)
    print (b)
    while(c<n):
        c=a+b
        print (c)
        a = b
        b = c
fibonacci(10)