# xunit.py

class TestResult:
    # ... (código existente, sem alterações)
    def __init__(self):
        self.run_count = 0; self.failures = []; self.errors = []
    def summary(self): return f"{self.run_count} run, {len(self.failures)} failed, {len(self.errors)} error"
    def test_started(self): self.run_count += 1
    def add_failure(self, test): self.failures.append(test)
    def add_error(self, test): self.errors.append(test)

class TestCase:
    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    # --- Novos Métodos de Assert ---
    def assert_equal(self, first, second):
        if first != second:
            raise AssertionError(f"{first} != {second}")

    def assert_true(self, expr):
        if not expr:
            raise AssertionError(f"{expr} is not true")

    def assert_false(self, expr):
        if expr:
            raise AssertionError(f"{expr} is not false")
            
    def assert_in(self, member, container):
        if member not in container:
            raise AssertionError(f"{member} not found in {container}")

    def set_up(self): pass
    def tear_down(self): pass
    def run(self, result):
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.test_method_name)
            method()
        except AssertionError as e:
            result.add_failure(f"{self.test_method_name}: {e}")
        except Exception as e:
            result.add_error(f"{self.test_method_name}: {e}")
        self.tear_down()

class TestSuite:
    # ... (código existente, sem alterações)
    def __init__(self): self.tests = []
    def add_test(self, test): self.tests.append(test)
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestLoader:
    # ... (código existente, sem alterações)
    TEST_METHOD_PREFIX = 'test'
    def get_test_case_names(self, test_case_class):
        methods = dir(test_case_class)
        test_names = filter(lambda m: m.startswith(self.TEST_METHOD_PREFIX), methods)
        return sorted(list(test_names))
    def make_suite(self, test_case_class):
        suite = TestSuite()
        for test_name in self.get_test_case_names(test_case_class):
            suite.add_test(test_case_class(test_name))
        return suite

class TestRunner:
    # ... (código existente, sem alterações)
    def __init__(self): self.result = TestResult()
    def run(self, test):
        test.run(self.result)
        print(self.result.summary())
        return self.result