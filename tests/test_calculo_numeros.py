import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'
    )
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='0')
    def test_ingreso_cero(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 0)

    @patch('builtins.input', return_value='  42  ')
    def test_ingreso_con_espacios(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 42)

    @patch('builtins.input', return_value='-9999')
    def test_ingreso_numero_muy_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='3.14')
    def test_ingreso_decimal(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

    @patch('builtins.input', return_value='123abc')
    def test_ingreso_alfanumerico(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()


    


if __name__ == '__main__':
    unittest.main() 