import subprocess
import unittest

class TestRPNFuncional(unittest.TestCase):
    def run_rpn(self, args, input_str=None):
        """Ejecuta el programa rpn.py como un proceso externo."""
        cmd = ["python", "rpn.py"] + args
        process = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input=input_str)
        return stdout.strip(), stderr.strip()

    def test_argumentos_linea_comandos(self):
        """Caso 1: Pasando la expresión como argumentos de CLI."""
        result, _ = self.run_rpn(["3", "4", "+"])
        self.assertEqual(result, "7.0")

    def test_entrada_estandar_stdin(self):
        """Caso 2: Usando input() interactivo."""
        result, _ = self.run_rpn([], input_str="5 1 2 + 4 * + 3 -")
        # El programa imprime el prompt 'RPN> ' antes del resultado
        self.assertIn("14.0", result)

    def test_operaciones_complejas(self):
        """Caso 3: Validación de funciones y constantes."""
        # (3^2) + sqrt(9) = 9 + 3 = 12
        result, _ = self.run_rpn(["3", "2", "yx", "9", "sqrt", "+"])
        self.assertEqual(result, "12.0")

    def test_manejo_errores_funcional(self):
        """Caso 4: Verificación de que los errores se muestran al usuario."""
        result, _ = self.run_rpn(["3", "0", "/"])
        self.assertIn("Error: División por cero", result)

if __name__ == "__main__":
    unittest.main()