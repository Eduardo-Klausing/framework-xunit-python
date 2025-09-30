# xunit.py

class TestResult:
    # ... (código existente, sem alterações)
    def __init__(self):
        self.run_count = 0
        self.failures = []
        self.errors = []

    def test_started(self):
        self.run_count += 1

    def add_failure(self, test_method_name):
        self.failures.append(test_method_name)

    def add_error(self, test_method_name):
        self.errors.append(test_method_name)

    def summary(self):
        return f"{self.run_count} run, {len(self.failures)} failed, {len(self.errors)} error"

class TestCase:
    # ... (código existente, sem alterações)
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.test_method_name)
            method()
        except AssertionError:
            result.add_failure(self.test_method_name)
        except Exception:
            result.add_error(self.test_method_name)
        
        self.tear_down()

class TestSuite:
    """
    Uma suíte de testes que agrupa múltiplos TestCases (ou outras TestSuites).
    Utiliza o padrão Composite, tendo o mesmo método run() que TestCase.
    """
    def __init__(self):
        self.tests = []

    def add_test(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            test.run(result)