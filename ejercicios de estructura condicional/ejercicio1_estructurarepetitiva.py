num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))

pares = 0
impares = 0
suma_pares = 0

if num1 % 2 == 0:
    pares += 1
    suma_pares += num1
else:
    impares += 1

if num2 % 2 == 0:
    pares += 1
    suma_pares += num2
else:
    impares += 1

if num3 % 2 == 0:
    pares += 1
    suma_pares += num3
else:
    impares += 1

if num4 % 2 == 0:
    pares += 1
    suma_pares += num4
else:
    impares += 1

print("Hay", pares, "números pares y", impares, "números impares")
print("La sumatoria de los números pares es", suma_pares)