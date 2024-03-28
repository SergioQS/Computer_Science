n = int(input())
i = 1
if n % 2 == 1:
    while i+4 < n:
        print(i+4)
        print(i+2)
        i = i + 2
    print(n)
if n % 2 == 0:
    while i+4 < n-1:
        print(i+4)
        print(i+2)
        i = i + 2
    print(n-1)
