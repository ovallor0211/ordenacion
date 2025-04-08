# Archivo: tres valores.py
# Fecha: 08/04/2025
# Proy: estudio de algoritmos.

# Función swap(int indice)
# cambia He ordena dos elementos de una lista ya existentes 
#
def swap(indice):
    a = s[indice]
    s[indice] = s[indice+1]
    s[indice+1] = a

n = []

# Rutina para tomar datos del teclado y guardarlos en la variable n de tipo lista
for i in range(3):
    n.append(int(input()))

s = n 
for i in range(2): 
    if s[i] > s[i+1]:
        a = s[i]
        s[i] = s[j+1]
        s[i+1] = a

s = n
for i in range(len(n)-2):
    for j in range(len(n)-1):
        if s[j] > s[j+1]:
            swap(j)
print(s)