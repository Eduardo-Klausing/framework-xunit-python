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
        self.log = ""
    def set_up(self): self.log += "set_up "
    def test_method(self): self.log += "test_method "
    def tear_down(self): self.log += "tear_down"

# --- Classes de Teste ---
class TestCaseTest(TestCase):
    # (8 testes existentes, sem alterações)
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
    def test_template_method(self):
        spy = TestSpy('test_method')
        spy.run(self.result)
        assert "set_up test_method tear_down" == spy.log

class TestSuiteTest(TestCase):
    # (3 testes existentes, sem alterações)
    def test_suite_multiple_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        suite.run(result)
        assert '2 run, 1 failed, 0 error' == result.summary()
    def test_suite_size(self):
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.add_test(TestStub('test_failure'))
        assert 2 == len(suite.tests)
    def test_suite_success_run(self):
        result = TestResult()
        suite = TestSuite()
        suite.add_test(TestStub('test_success'))
        suite.run(result)
        assert '1 run, 0 failed, 0 error' == result.summary()

class TestLoaderTest(TestCase):
    def test_create_suite(self):
        loader = TestLoader()
        suite = loader.make_suite(TestStub)
        assert 3 == len(suite.tests)
    
    def test_get_multiple_test_case_names(self):
        loader = TestLoader()
        names = loader.get_test_case_names(TestStub)
        assert ['test_error', 'test_failure', 'test_success'] == names

    def test_get_no_test_case_names(self):
        class Test(TestCase):
            def foobar(self):
                pass
        loader = TestLoader()
        names = loader.get_test_case_names(Test)
        assert [] == names

# --- Bloco de Execução Final ---
if __name__ == "__main__":
    all_tests_suite = TestSuite()
    loader = TestLoader()
    
    all_tests_suite.add_test(loader.make_suite(TestCaseTest))
    all_tests_suite.add_test(loader.make_suite(TestSuiteTest))
    all_tests_suite.add_test(loader.make_suite(TestLoaderTest))

    runner = TestRunner()
    runner.run(all_tests_suite)