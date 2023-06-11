a= float(input("Introduce el primer lado del triángulo:"))
b = float(input("Introduce el segundo lado del triángulo:"))
c = float(input("Introduce el tercer lado del triángulo:"))

if a==b==c:
    print("El triángulo es equilátero")
elif a == b or a == c or b == c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")