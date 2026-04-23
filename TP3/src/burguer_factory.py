from abc import ABC, abstractmethod


class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self):
        """Realiza la entrega y devuelve un mensaje"""
        pass


class HamburguesaMostrador(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa entregada en mostrador"


class HamburguesaRetiro(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa retirada por el cliente"


class HamburguesaDelivery(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa enviada por delivery"


class HamburguesaFactory:

    @staticmethod
    def cocinar_hamburguesa(tipo: str) -> Hamburguesa:
        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "mostrador":
            return HamburguesaMostrador()
        elif tipo_normalizado == "retiro":
            return HamburguesaRetiro()
        elif tipo_normalizado == "delivery":
            return HamburguesaDelivery()
        else:
            raise ValueError(
                f"Tipo de hamburguesa no válido: '{tipo}'\n" 
                "Opciones válidas: 'mostrador', 'retiro', 'delivery'"
            )

def main() -> None:
    tipos = ["mostrador", "retiro", "delivery", "pizza"]

    for tipo in tipos:
        try:
            hamburguesa = HamburguesaFactory.cocinar_hamburguesa(tipo)
            print(f"{tipo} -> {hamburguesa.entregar()}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
