"""
3. Supón que un ramo tiene las siguientes evaluaciones:

• 3 tareas en Laboratorio, estas valen un 15% del curso,
• 3 tareas en clase, que valen un 15% del curso, y 2 notas solemnes cada una un 35%

Elabora un programa que, ingresando todas las notas, entregue la nota de presentación.
Ejemplo:
Lab 1 = 4.5
Lab 2 = 7.0
Lab 3 = 5.5
Tarea 1 = 6.2
Tarea 2 = 5.0
Tarea 3 = 2.1
Solemne 1 = 1.8
Solemne 2 = 5.4
Nota de presentación = (Prom Lab)*0,15 + (Prom Tareas)*0.15 + Sol1*0.35 + Sol2*0.35
Prom Lab = 5.7
Prom Tarea = 4.4
Nota de presentación = 5.7*0.15 + 4.4*0.15 + 1.8*0.35 + 5.4*0.35 
Nota de presentación = 4.0
"""

"""
Elaboración de mi algoritmo

1. Solicitar al usuario que ingrese las 3 notas del Laboratorio
2. Solicitar al usuario que ingrese las 3 notas de las tareas en clase
3. Solicitar al usuario que ingrese las 2 notas Solemnes
4. Calcular el promedio de las notas de laboratiorio y multiplicarlo por el 15% o por 0.15
5. Calcular el promedio de las notas de las tareas y multiplicarlo por el 15% o el 0.15
6. Calcular el valor de cada nota solmne por el 35% o 0.35
7. Sumar los resultados de Laboratorio, tareas y notas solemnes, para obtener la nota final
8. Mostrar nota final de presentación.
"""

print("Ingrese las 3 notas del Laboratorio")
lab1 = float(input ("Ingrese la nota 1 del laboratorio: "))
lab2 = float(input ("Ingrese la nota 2 del laboratorio: "))
lab3 = float(input ("Ingrese la nota 3 del laboratorio: "))

