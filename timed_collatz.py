import time

def collatz_rec(n, l=1):
    
    if n == 1:
        
        return l#, t_end - t_start
    elif n % 2 == 0:
        return collatz_rec(n / 2, l + 1)
    else:
        return collatz_rec(3 * n + 1, l + 1)

def collatz_nonrec(n):
    
    l = 1
    while n != 1:
        l += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    
    return l#, t_end - t_start
#t_start = time.clock()
#max_l = max([collatz_rec(i) for i in range(1, 1000000)])
#t_end = time.clock()
#timed_rec = t_end - t_start
#t_start = time.clock()
#max_l = max([collatz_nonrec(i) for i in range(1, 1000000)])
s = sum([collatz_nonrec(i) for i in range(1, 11)])
#t_end = time.clock()
#timed_nonrec = t_end - t_start
print(s)
#print(timed_rec - timed_nonrec)