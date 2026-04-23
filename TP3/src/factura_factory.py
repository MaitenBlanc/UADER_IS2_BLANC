# Implemente una clase “factura” que tenga un importe correspondiente al total
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
# condición.

from abc import ABC, abstractmethod


class Factura(ABC):
    def __init__(self, importe: float):
        self.importe = importe
    
    @abstractmethod
    def emitir_factura(self) -> str:
        pass
    
class FacturaIVAResponsable(Factura):
    def emitir_factura(self) -> str:
        return f"Factura para IVA Responsable - Importe Total: ${self.importe:.2f}"


class FacturaIVANoInscripto(Factura):
    def emitir_factura(self) -> str:
        return f"Factura para IVA No Inscripto - Importe Total: ${self.importe:.2f}"


class FacturaIVAExento(Factura):
    def emitir_factura(self) -> str:
        return f"Factura para IVA Exento - Importe Total: ${self.importe:.2f}"

class FacturaFactory: 
    @staticmethod
    def crear_factura(tipo: str, importe: float) -> Factura:
        tipo_normalizado = tipo.strip().lower()
        
        if tipo_normalizado == "iva responsable":
            return FacturaIVAResponsable(importe)
        elif tipo_normalizado == "iva no inscripto":
            return FacturaIVANoInscripto(importe)
        elif tipo_normalizado == "iva exento":
            return FacturaIVAExento(importe)
        else:
            raise ValueError(
                f"Tipo de IVA no válida: '{tipo}'\n" 
                "Opciones válidas: 'iva responsable', 'iva no inscripto', 'iva exento'"
            )

# Prueba
def main():
    tipos = ["iva responsable", "iva no inscripto", "iva exento", "iva no valido"]
    
    for tipo in tipos:
        try:
            factura = FacturaFactory.crear_factura(tipo, 1000)
            print(f"{tipo!r} -> {factura.emitir_factura()}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()