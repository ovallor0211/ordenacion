e = [7, 5, 3]

if e[0] > e[1]:
    a = e[0]
    e[0] = e[1]
    e[1] = a

if e[1] > e[2]:
    a = e[1]
    e[1] = e[2]
    e[2] = a

if e[0] > e[1]:
    a = e[0]
    e[0] = e[1]
    e[1] = a
print(e)