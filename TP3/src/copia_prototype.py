import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
    
class DocumentoClonable(Prototype):
    def __init__(self, nombre: str, datos: list):
        self.nombre = nombre
        self.datos = datos

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self) -> str:
        return f"Documento: \nNombre: {self.nombre}\nDatos: {self.datos}"
    
def main() -> None:
    doc_original = DocumentoClonable(
        nombre = "Informe",
        datos = ["Sección 1"]
    )
    
    print('----- Documento original -----')
    print(doc_original)
    
    # Copia 1
    doc_clonado1 = doc_original.clone()
    doc_clonado1.nombre = "Informe Clonado 1"
    doc_clonado1.datos.append("Sección 2")
    
    print('----- Documento 1 - Clonado del original -----')
    print(doc_clonado1)
    
    # Copia 2
    doc_clonado2 = doc_clonado1.clone()
    doc_clonado2.nombre = "Informe Clonado 2"
    doc_clonado2.datos.append("Sección 3")
    
    print('----- Documento 2 - Clonado de la copia 1 -----')
    print(doc_clonado2)
    
    # Verifico la independencia
    print('\n----- Verificación Final de Independencia -----')
    print(f"ID Original: {id(doc_original)}")
    print(f"ID Clon 1:   {id(doc_clonado1)}")
    print(f"ID Clon 2:   {id(doc_clonado2)}")

if __name__ == "__main__":
    main()