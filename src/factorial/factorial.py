#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys
def factorial(num):
    if num < 0:
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0:
        return 1

    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

# Modificación 1: Si no se pasa argumento
if len(sys.argv) < 2:
    num = input("Debe informar un número: ")
else:
    num = sys.argv[1]
# Fin modificación 1

# Modificación 2 y 3: aceptar números de un rango
if "-" in num:
    # Divido la entrada del input para poder guardar los 2 números del rango
    partes = num.split("-")
    
    # Verifico si el límite inferior está vacío
    if partes[0] == "": 
        num1 = 1    
    else:
        num1 = int(partes[0])
    
    # Verifico si el límite superior está vacío
    if partes[1] == "":
        num2 = 60
    else:
        num2 = int(partes[1])
        
    # Itero con los límites que obtuve anteriormente (puede ser inf-sup, inf- o -sup)
    for i in range(num1, num2 + 1):
        print("Factorial ", i, "! es ", factorial(i))
else:
    # Capto y muestro el factorial cuando sólo se pasa un número en particular
    num = int(num)
    print("Factorial ", num, "! es ", factorial(num))
# Fin modificación 2 y 3
