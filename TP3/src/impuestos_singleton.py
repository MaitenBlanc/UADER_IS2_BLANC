from threading import Lock


class CalculadoraImpuestos:
    _instancia = None
    _lock = Lock()
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not hasattr(self, "_inicializado"):
            self._inicializado = True
    
    def calcular_impuestos(self, base_imponible: float) -> float:
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return iva + iibb + contribuciones
    
# Prueba
def main():
    calc1 = CalculadoraImpuestos()
    calc2 = CalculadoraImpuestos()

    print(f"¿Son la misma instancia? {calc1 is calc2}")
    print(f"Impuestos de 1000: {calc1.calcular_impuestos(1000)}")
    print(f"Impuestos de 2000: {calc1.calcular_impuestos(2000)}")
    print(f"Impuestos de 3300: {calc1.calcular_impuestos(3300)}")
    
if __name__ == "__main__":
    main()