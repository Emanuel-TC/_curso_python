import unittest
import cambia_texto


class ProbarUnittest(unittest.TestCase):

    def test_mayusculas(self):
        palabra = "hola mundo"
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, "HOLA MUNDO")

if __name__ == '__main__':
    unittest.main()
