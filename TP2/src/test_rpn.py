import unittest
from rpn import eval_rpn, RPNError
import math


class TestRPN(unittest.TestCase):

    # ------------------------
    # CASOS CORRECTOS
    # ------------------------
    def test_operaciones(self):
        self.assertEqual(eval_rpn("3 4 +".split()), 7)
        self.assertEqual(eval_rpn("5 1 2 + 4 * + 3 -".split()), 14)
        self.assertEqual(eval_rpn("2 3 4 * +".split()), 14)
        self.assertEqual(eval_rpn("8 2 /".split()), 4)

    def test_floats_y_negativos(self):
        self.assertAlmostEqual(eval_rpn("2.5 2 *".split()), 5.0)
        self.assertEqual(eval_rpn("-3 2 *".split()), -6)

    def test_funciones(self):
        self.assertEqual(eval_rpn("9 sqrt".split()), 3)
        self.assertEqual(eval_rpn("100 log".split()), 2)
        self.assertAlmostEqual(eval_rpn("2.718281828 ln".split()), 1, places=3)
        self.assertEqual(eval_rpn("2 3 yx".split()), 8)
        self.assertEqual(eval_rpn("2 1/x".split()), 0.5)
        self.assertEqual(eval_rpn("2 10x".split()), 100)

    def test_trig(self):
        self.assertAlmostEqual(eval_rpn("90 sin".split()), 1, places=5)
        self.assertAlmostEqual(eval_rpn("0 cos".split()), 1, places=5)
        self.assertAlmostEqual(eval_rpn("45 tg".split()), 1, places=5)

    def test_pila(self):
        self.assertEqual(eval_rpn("3 dup *".split()), 9)
        self.assertEqual(eval_rpn("3 4 swap -".split()), 1)
        self.assertEqual(eval_rpn("3 4 drop".split()), 3)

    def test_memoria(self):
        self.assertEqual(eval_rpn("5 01 sto 01 rcl".split()), 5)

    # ------------------------
    # ERRORES (CON TRY/EXCEPT)
    # ------------------------

    def test_division_por_cero(self):
        try:
            eval_rpn("3 0 /".split())
            self.fail("Se esperaba excepción por división por cero")
        except RPNError as e:
            self.assertIn("cero", str(e).lower())

    def test_token_invalido(self):
        try:
            eval_rpn("2 3 &".split())
            self.fail("Se esperaba excepción por token inválido")
        except RPNError as e:
            self.assertIn("token", str(e).lower())

    def test_pila_insuficiente(self):
        try:
            eval_rpn("+".split())
            self.fail("Se esperaba excepción por pila insuficiente")
        except RPNError as e:
            self.assertIn("pila", str(e).lower())

    def test_pila_final_invalida(self):
        try:
            eval_rpn("2 3".split())
            self.fail("Se esperaba error por pila final inválida")
        except RPNError as e:
            self.assertIn("exactamente un valor", str(e).lower())

    def test_sqrt_negativo(self):
        try:
            eval_rpn("-1 sqrt".split())
            self.fail("Se esperaba error de raíz negativa")
        except RPNError as e:
            self.assertIn("negativa", str(e).lower())

    def test_log_invalido(self):
        try:
            eval_rpn("0 log".split())
            self.fail("Se esperaba error log inválido")
        except RPNError as e:
            self.assertIn("log", str(e).lower())

    def test_ln_invalido(self):
        try:
            eval_rpn("-1 ln".split())
            self.fail("Se esperaba error ln inválido")
        except RPNError as e:
            self.assertIn("ln", str(e).lower())

    def test_swap_insuficiente(self):
        try:
            eval_rpn("1 swap".split())
            self.fail("Se esperaba error en swap")
        except RPNError as e:
            self.assertIn("pila", str(e).lower())

    def test_memoria_invalida(self):
        try:
            eval_rpn("5 10 sto".split())
            self.fail("Se esperaba error de memoria inválida")
        except RPNError as e:
            self.assertIn("memoria", str(e).lower())

    def test_clear_pila_final(self):
        try:
            eval_rpn("3 4 clear".split())
            self.fail("Se esperaba error por pila vacía al final")
        except RPNError as e:
            self.assertIn("exactamente un valor", str(e).lower())


if __name__ == "__main__":
    unittest.main()