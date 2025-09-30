# xunit.py

class TestResult:
    # ... (código existente, sem alterações)
    def __init__(self):
        self.run_count = 0
        self.failures = []
        self.errors = []
    def summary(self):
        return f"{self.run_count} run, {len(self.failures)} failed, {len(self.errors)} error"
    # ... (outros métodos)
    def test_started(self): self.run_count += 1
    def add_failure(self, test): self.failures.append(test)
    def add_error(self, test): self.errors.append(test)

class TestCase:
    # ... (código existente, sem alterações)
    def __init__(self, test_method_name): self.test_method_name = test_method_name
    def set_up(self): pass
    def tear_down(self): pass
    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.test_method_name)
            method()
        except AssertionError: result.add_failure(self.test_method_name)
        except Exception: result.add_error(self.test_method_name)
        self.tear_down()

class TestSuite:
    # ... (código existente, sem alterações)
    def __init__(self): self.tests = []
    def add_test(self, test): self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestLoader:
    TEST_METHOD_PREFIX = 'test'

    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        test_names = filter(lambda m: m.startswith(self.TEST_METHOD_PREFIX), methods)
        return sorted(list(test_names))

    def make_suite(self, test_case_class):
        suite = TestSuite()
        for test_name in self.get_test_case_names(test_case_class):
            test_case = test_case_class(test_name)
            suite.add_test(test_case)
        return suite

class TestRunner:
    def __init__(self):
        self.result = TestResult()

    def run(self, test):
        test.run(self.result)
        print(self.result.summary())
        return self.result