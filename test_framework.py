# test_framework.py

from xunit import TestCase, TestResult

# --- Classes de Suporte para os Testes ---

class TestStub(TestCase):
    def test_success(self):
        assert True

    def test_failure(self):
        assert False

    def test_error(self):
        raise ValueError("This is an error")

class TestSpy(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.was_set_up = False
        self.was_run = False
        self.was_tear_down = False
        self.log = ""

    def set_up(self):
        self.was_set_up = True
        self.log += "set_up "

    def test_method(self):
        self.was_run = True
        self.log += "test_method "

    def tear_down(self):
        self.was_tear_down = True
        self.log += "tear_down"

# --- Classe de Teste para o TestCase ---

class TestCaseTest(TestCase):
    def set_up(self):
        self.result = TestResult()

    # Testes com TestStub (4 métodos)
    def test_result_success_run(self):
        stub = TestStub('test_success')
        stub.run(self.result)
        assert '1 run, 0 failed, 0 error' == self.result.summary()

    def test_result_failure_run(self):
        stub = TestStub('test_failure')
        stub.run(self.result)
        assert '1 run, 1 failed, 0 error' == self.result.summary()

    def test_result_error_run(self):
        stub = TestStub('test_error')
        stub.run(self.result)
        assert '1 run, 0 failed, 1 error' == self.result.summary()

    def test_result_multiple_run(self):
        TestStub('test_success').run(self.result)
        TestStub('test_failure').run(self.result)
        TestStub('test_error').run(self.result)
        assert '3 run, 1 failed, 1 error' == self.result.summary()

    # Testes com TestSpy (4 métodos)
    def test_was_set_up(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_set_up

    def test_was_run(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_run

    def test_was_tear_down(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert spy.was_tear_down

    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert "set_up test_method tear_down" == spy.log

# --- Bloco de Execução ---

if __name__ == "__main__":
    result = TestResult()
    
    # Executa todos os 8 testes da classe TestCaseTest
    TestCaseTest('test_result_success_run').run(result)
    TestCaseTest('test_result_failure_run').run(result)
    TestCaseTest('test_result_error_run').run(result)
    TestCaseTest('test_result_multiple_run').run(result)
    
    TestCaseTest('test_was_set_up').run(result)
    TestCaseTest('test_was_run').run(result)
    TestCaseTest('test_was_tear_down').run(result)
    TestCaseTest('test_template_method').run(result)
    
    # Imprime o sumário final dos testes do framework
    print(result.summary())