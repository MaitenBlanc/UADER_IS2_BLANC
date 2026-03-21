#!/usr/bin/python
# *-------------------------------------------------------------------------*
# * factorial.py                                                            *
# * calcula el factorial de un número                                       *
# * Dr.P.E.Colla (c) 2022                                                   *
# * Creative commons                                                        *
# *-------------------------------------------------------------------------*
import sys
class Factorial:
    def __init__(self):
        pass

    def calcular_factorial(self, num):
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

    def run(self, min, max):
        for i in range(min, max + 1):
            print("Factorial ", i, "! es ", self.calcular_factorial(i))

# Si no se pasa argumento
if len(sys.argv) < 2:
    num = input("Debe informar un número: ")
else:
    num = sys.argv[1]

# Instancia de la clase
calc = Factorial()

# Aceptar números de un rango
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

    # Itero con los límites que obtuve anteriormente (puede ser inf-sup, inf- o -sup) usando el método declarado en la clase Factorial
    calc.run(num1, num2)

else:
    # Si se pasa como argunmento un solo número, min y máx son el mismo número.
    numero = int(num)
    calc.run(numero, numero)
