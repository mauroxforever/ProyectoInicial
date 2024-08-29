

# Comentarios, este queda solo en la misma linea en la que se utiliza "gato"

"""
hola esto tambien es un comentario
de varias lineas
jojojo dentro de 3 comillas
"""

# esto será una calculadora


def sumar (a,b):
    return a + b

def restar (a,b):
    return a - b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    return a/b

print("Bienvenido a mi calculadora")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

eleccion = int(input("Elija una opción: "))

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if eleccion == 1:
    print (num1, "+", num2, "=", sumar(num1,num2))

elif eleccion == 2: 
    print (num1, "+", num2, "=", restar(num1,num2))

elif eleccion == 3: 
    print (num1, "+", num2, "=", multiplicar(num1,num2))

elif eleccion == 4: 
    print (num1, "+", num2, "=", dividir(num1,num2))

elif eleccion == 5:
    print("Gracias por utilizar mi calculadora, Hasta pronto!")

else:
    print("Eliga una opción valida!!")



