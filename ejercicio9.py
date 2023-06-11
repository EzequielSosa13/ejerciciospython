número1 = int(input("Introduce el primer número: "))
número2 = int(input("Introduce el segundo número: "))
número3 = int(input("Introduce el tercer número: "))

if número1 > número2 and número1 > número3:
    mayor = número1
elif número2 > número1 and número2 > número3:
    mayor = número2
else:
    mayor = número3

if mayor % 2 == 0:
    print("El número mayor es", mayor, "y es par")
else:
    print("El número mayor es", mayor, "y es impar")
