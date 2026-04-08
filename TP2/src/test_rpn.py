import unittest
from rpn import eval_rpn, RPNError
import math


class TestRPN(unittest.TestCase):

    # ------------------------
    # OPERACIONES BÁSICAS
    # ------------------------
    def test_suma(self):
        self.assertEqual(eval_rpn("3 4 +".split()), 7)

    def test_expresion_compleja(self):
        self.assertEqual(eval_rpn("5 1 2 + 4 * + 3 -".split()), 14)

    def test_multiplicacion(self):
        self.assertEqual(eval_rpn("2 3 4 * +".split()), 14)

    def test_division(self):
        self.assertEqual(eval_rpn("8 2 /".split()), 4)

    def test_floats(self):
        self.assertAlmostEqual(eval_rpn("2.5 2 *".split()), 5.0)

    def test_negativos(self):
        self.assertEqual(eval_rpn("-3 2 *".split()), -6)

    # ------------------------
    # ERRORES
    # ------------------------
    def test_division_por_cero(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 0 /".split())

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            eval_rpn("2 3 &".split())

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            eval_rpn("+".split())

    def test_pila_final_invalida(self):
        with self.assertRaises(RPNError):
            eval_rpn("2 3".split())

    # ------------------------
    # FUNCIONES
    # ------------------------
    def test_sqrt(self):
        self.assertEqual(eval_rpn("9 sqrt".split()), 3)

    def test_log(self):
        self.assertEqual(eval_rpn("100 log".split()), 2)

    def test_ln(self):
        self.assertAlmostEqual(eval_rpn("2.718281828 ln".split()), 1, places=3)

    def test_ex(self):
        self.assertAlmostEqual(eval_rpn("1 ex".split()), math.e)

    def test_potencia(self):
        self.assertEqual(eval_rpn("2 3 yx".split()), 8)

    def test_inverso(self):
        self.assertEqual(eval_rpn("2 1/x".split()), 0.5)

    def test_10x(self):
        self.assertEqual(eval_rpn("2 10x".split()), 100)

    def test_chs(self):
        self.assertEqual(eval_rpn("5 chs".split()), -5)

    # ------------------------
    # TRIGONOMETRÍA
    # ------------------------
    def test_sin(self):
        self.assertAlmostEqual(eval_rpn("90 sin".split()), 1, places=5)

    def test_cos(self):
        self.assertAlmostEqual(eval_rpn("0 cos".split()), 1, places=5)

    def test_tg(self):
        self.assertAlmostEqual(eval_rpn("45 tg".split()), 1, places=5)

    # ------------------------
    # PILA
    # ------------------------
    def test_dup(self):
        self.assertEqual(eval_rpn("3 dup *".split()), 9)

    def test_swap(self):
        self.assertEqual(eval_rpn("3 4 swap -".split()), 1)

    def test_drop(self):
        self.assertEqual(eval_rpn("3 4 drop".split()), 3)

    def test_clear_error(self):
        with self.assertRaises(RPNError):
            eval_rpn("3 4 clear".split())

    # ------------------------
    # MEMORIA
    # ------------------------
    def test_sto_rcl(self):
        self.assertEqual(eval_rpn("5 01 sto 01 rcl".split()), 5)

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            eval_rpn("5 10 sto".split())


if __name__ == "__main__":
    unittest.main()