# se trata de tomar una lista de dso valores desordenados
# y producir una salida de orden creciente

n = [65, 23]
if n[0] > n[1]:
    a = n[0]
    n[0] = n[1]
    n[1] = a
    print(n)
else:
    print(n)