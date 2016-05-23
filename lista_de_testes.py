import unittest

from Fibonacci import (fibonacci)
from Media import media
from Fatorial import fatorial


class TestaFuncoes(unittest.TestCase):
    def test_Fiboonaci_dez(self):
        self.assertEqual(55,fibonacci(10))
    def test_Fiboonaci_um(self):
        self.assertEqual(1,fibonacci(1))
    def test_Fiboonaci_zero(self):
        self.assertEqual(0,fibonacci(0))
    def test_Fatorial_dez(self):
        self.assertEqual(3628800,fatorial(10))
    def test_Fatorial_um(self):
        self.assertEqual(1,fatorial(1))
    def test_Fatorial_zero(self):
        self.assertEqual(1,fatorial(0))
    def test_Media_10(self):
        lista=(10,10)
        self.assertEqual(10,media(lista))
    def test_Media_tres(self):
        lista=(3,3,3)
        self.assertEqual(3,media(lista))
unittest.main()
