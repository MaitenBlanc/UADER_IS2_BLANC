import math

class CalculadoraFactorial:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraFactorial, cls).__new__(cls)
        return cls._instancia

    def calcular_factorial(self, n):
        if n < 0:
            return "El número debe ser positivo"
        return math.factorial(n)

# Prueba
calc1 = CalculadoraFactorial()
calc2 = CalculadoraFactorial()

print(f"¿Son la misma instancia? {calc1 is calc2}")
print(f"Factorial de 5: {calc1.calcular_factorial(5)}")
print(f"Factorial de 8: {calc1.calcular_factorial(8)}")
print(f"Factorial de 3: {calc1.calcular_factorial(3)}")