# Elabore una clase para el cálculo del valor de impuestos a ser utilizado por
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado
# deberá recibir un valor de importe base imponible y deberá retornar la suma
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre
# esa base imponible.


class CalculadoraImpuestos:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instancia
    
    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return iva + iibb + contribuciones
    
# Prueba
calc1 = CalculadoraImpuestos()
calc2 = CalculadoraImpuestos()

print(f"¿Son la misma instancia? {calc1 is calc2}")
print(f"Impuestos de 1000: {calc1.calcular_impuestos(1000)}")
print(f"Impuestos de 2000: {calc1.calcular_impuestos(2000)}")
print(f"Impuestos de 3300: {calc1.calcular_impuestos(3300)}")