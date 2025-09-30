# test_framework.py

from xunit import TestCase, TestResult

class MyTest(TestCase):
    def set_up(self):
        print("set_up")

    def tear_down(self):
        print("tear_down")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")

if __name__ == "__main__":
    # 1. Cria um objeto para coletar os resultados
    result = TestResult()

    # 2. Cria as instâncias de teste e as executa, passando o objeto de resultado
    MyTest('test_a').run(result)
    MyTest('test_b').run(result)
    MyTest('test_c').run(result)

    # 3. Imprime o sumário no final
    print(result.summary())