#clase 21/3/2023

#Uso For
"""
for i in range(11):
    print(i)

for i in range(2,5):
    print(i)
"""

#Uso While
"""
i = 0
while i < 6:

    if i == 3:
        print(f"Encontre el valor: {i}")
        i += 1
        continue #Continua el proceso sin ejecutar lo que se encuentra fuera

    print(f"El valor es: {i}")
    i += 1
"""


"""
import random

numero = random.randint(1,5)
print(numero)

text = "CURSO PYTHON"
letra = random.choice(text)
print(letra)

"""

#Listas
caja = [1, "Python", 2, "Criss", True]
print(caja)

caja.append("Java")
print(caja)

caja.insert(1, "Angular")
print(caja)

caja.pop(6)
print(caja)

caja.remove(2)
print(caja)

print(caja[3])

caja[2] = "Python2"
print(caja)

index = caja.index("Criss")
print(index)

for i in caja:
    print(f"Elemento de la lista: {i}")

#Tuplas - Lista Inmutable -- Velocidad de procesamiento
tup = (1,2,3,4,5)
print(tup)
