def f(s, x):
    if not x:
        print(s)
        return

    s2 = s
    s += '0'
    f(s, x-1)
    s2 += '1'
    f(s2, x-1)


n = int(input())
f('', n)