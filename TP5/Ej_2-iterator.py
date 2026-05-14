from collections.abc import Iterable, Iterator


# Clase Iterator
class StringIterator(Iterator):
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        # El índice inicia al final si es reverso, o al principio si es directo
        self._index = len(collection) - 1 if reverse else 0

    def __next__(self):
        # Validación: Detener si el índice sale de los límites (0)
        if self._reverse and self._index < 0:
            raise StopIteration()
        
        try:
            value = self._collection[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


# Clase de Colección
class CadenaCaracteres(Iterable):
    def __init__(self, texto: str):
        self._texto = texto

    def __iter__(self) -> StringIterator:
        # Sentido directo por defecto
        return StringIterator(self._texto)

    def get_reverse_iterator(self) -> StringIterator:
        # Sentido reverso
        return StringIterator(self._texto, True)


if __name__ == "__main__":
    mi_cadena = CadenaCaracteres("Hola Mundo")

    print("Recorrido Directo:")
    for char in mi_cadena:
        print(char, end="")

    print("\nRecorrido Reverso:")
    for char in mi_cadena.get_reverse_iterator():
        print(char, end="")
    print()
