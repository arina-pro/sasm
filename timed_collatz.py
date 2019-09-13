import time

def collatz_rec(n, l=1):
    t_start = time.clock()
    if n == 1:
        t_end = time.clock()
        return l, t_end - t_start
    elif n % 2 == 0:
        return collatz_rec(n / 2, l + 1)
    else:
        return collatz_rec(3 * n + 1, l + 1)

def collatz_nonrec(n):
    t_start = time.clock()
    l = 1
    while n != 1:
        l += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    t_end = time.clock()
    return l, t_end - t_start

print(collatz_rec(1234))
print(collatz_nonrec(1234))