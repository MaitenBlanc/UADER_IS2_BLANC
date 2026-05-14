from abc import ABC, abstractmethod

# Clase base abstracta
class AbstractHandler(ABC):
    def __init__(self, nxt=None):
        self._nxt = nxt

    def handle(self, request):
        handled = self.processRequest(request)
        # Si no fue manejado y hay un siguiente en la cadena, pasar el número
        if not handled and self._nxt:
            self._nxt.handle(request)

    @abstractmethod
    def processRequest(self, request):
        raise NotImplementedError('Debe implementar este método')

# Manejador para números pares
class HandlerPares(AbstractHandler):
    def processRequest(self, request):
        if request % 2 == 0:
            print(f"Consumiendo número par: {request}")
            return True
        return False

# Manejador para números primos
class HandlerPrimos(AbstractHandler):
    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def processRequest(self, request):
        if self.is_prime(request):
            print(f"Consumiendo número primo: {request}")
            return True
        return False

# Manejador para números no consumidos
class DefaultHandler(AbstractHandler):
    def processRequest(self, request):
        print(f"El número {request} no fue consumido por ninguna clase.")
        return True

# Main
if __name__ == "__main__":
    # Construcción de la cadena: Pares -> Primos -> Default
    chain = HandlerPares(HandlerPrimos(DefaultHandler()))

    print("--- Procesando números del 1 al 100 ---")
    for i in range(1, 101):
        chain.handle(i)