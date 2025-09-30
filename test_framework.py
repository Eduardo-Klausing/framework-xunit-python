# test_framework.py

from xunit import TestCase

class MyTest(TestCase):
    """
    Uma classe de teste de exemplo que herda de TestCase para demonstrar
    o funcionamento do framework.
    """

    def set_up(self):
        """Sobrescreve o set_up para imprimir uma mensagem."""
        print("set_up")

    def tear_down(self):
        """Sobrescreve o tear_down para imprimir uma mensagem."""
        print("tear_down")

    def test_a(self):
        """Primeiro método de teste."""
        print("test_a")

    def test_b(self):
        """Segundo método de teste."""
        print("test_b")

    def test_c(self):
        """Terceiro método de teste."""
        print("test_c")

# Bloco de execução principal para rodar os testes
if __name__ == "__main__":

    test_a = MyTest('test_a')
    test_a.run()
    
    test_b = MyTest('test_b')
    test_b.run()
    
    test_c = MyTest('test_c')
    test_c.run()
    
 