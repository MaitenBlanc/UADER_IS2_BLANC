import matplotlib.pyplot as plt

# TP dice conjetura 2n + 1, pero yo voy a usar la fórmula real (3n + 1) para evitar loop infinito
min = 1
max = 10000

def calcular_iteraciones(n):
    iteraciones = 0
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    
    return iteraciones

# listas para almacenar datos de gráfico
n_val = []
iteraciones_val = []

# de 1 a 10000
for n in range(min, max + 1):
    n_val.append(n)
    iteraciones_val.append(calcular_iteraciones(n))
    
# Generación de gráfico
plt.plot(n_val, iteraciones_val)

# Valores para personalizar el gráfico
plt.title("Conjetura de Collatz")
plt.xlabel("Valor de n")
plt.ylabel("Número de iteraciones")
plt.grid(True)

plt.show()
