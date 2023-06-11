#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

Mayores100= 0
Menores100= 0
NumeroMaximo= float('-inf')  
NumeroMinimo= float('inf')  

for i in range(10):
    Numero= float(input("Ingrese un número:"))
    if Numero>100:
         Mayores100 += 1
    elif Numero<100:
        Menores100 += 1
    if Numero> NumeroMaximo:
        NumeroMaximo= Numero
    if Numero<NumeroMinimo:
        NumeroMinimo= Numero

print("Cantidad de números mayores a 100:", Mayores100)
print("Cantidad de números menores a 100:", Menores100)
print("Número máximo:", NumeroMaximo)
print("Número mínimo:", NumeroMinimo)