def next(a):
    b = a+1
    while True:
        
        h=0
        for i in range(2,b):

            if b % i == 0:
                h=h+1
                break
        if h == 0 and b>1:
            print(f"{b} is next immedate palindrome")
            break
        else :
            b = b+1
next(a=7)