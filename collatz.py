def collatz_rec(n):
    if n == 1:
        return []
    if n % 2 == 0:
        return [n] + collatz_rec(n//2)
    else:
        return [n] + collatz_rec(3*n+1)
