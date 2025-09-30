# test_framework.py

from xunit import TestCase, TestResult, TestSuite, TestLoader, TestRunner

# --- Classes de Suporte (sem alterações) ---
class TestStub(TestCase):
    def test_success(self): assert True
    def test_failure(self): assert False
    def test_error(self): raise ValueError("Error")

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

# --- Classes de Teste (VERSÃO FINAL E CORRIGIDA) ---
class TestCaseTest(TestCase):
    # CORRIGIDO: Agora com todos os 8 testes
    def set_up(self): self.result = TestResult()
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

class TestSuiteTest(TestCase):
    # (3 testes, sem alterações)
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        assert 3 == len(suite.tests)
    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        assert '1 run, 0 failed, 0 error' == result.summary()
    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.add_test(TestStub('test_error'))
        suite.run(result)
        assert '3 run, 1 failed, 1 error' == result.summary()

class TestLoaderTest(TestCase):
    # CORRIGIDO: Agora com todos os 4 testes
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        assert 3 == len(suite.tests)
    def test_create_suite_of_suites(self):
        loader = TestLoader()
        stub_suite = loader.make_suite(TestStub)
        spy_suite = loader.make_suite(TestSpy)
        suite = TestSuite()
        suite.add_test(stub_suite)
        suite.add_test(spy_suite)
        assert 2 == len(suite.tests)
    def test_get_multiple_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        assert ['test_error', 'test_failure', 'test_success'] == names
    def test_get_no_test_case_names(self):
        class Test(TestCase):
            def foobar(self): pass
        loader = TestLoader()
        names = loader.get_test_case_names(Test)
        assert [] == names

# --- Bloco de Execução Final ---
if __name__ == "__main__":
    loader = TestLoader()
    
    # Cria uma suíte principal para agrupar tudo
    suite = TestSuite()
    
    # Carrega automaticamente os testes de cada classe
    suite.add_test(loader.make_suite(TestCaseTest))
    suite.add_test(loader.make_suite(TestSuiteTest))
    suite.add_test(loader.make_suite(TestLoaderTest))

    # Executa tudo com o Runner
    runner = TestRunner()
    runner.run(suite)