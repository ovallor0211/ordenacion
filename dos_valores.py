n = [17, 6, 15]

if n[0] > n[1]:
    a = n[0]
    n[0] = n[1]
    n[1] = a

if n[1] > n[2]:
    a = n[1]
    n[1] = n[2]
    n[2] = a

if n[0] > n[1]:
    a = n[0]
    n[0] = n[1]
    n[1] = a

print(n)