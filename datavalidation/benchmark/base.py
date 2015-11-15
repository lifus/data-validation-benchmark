import benchmark
from datavalidation.libraries import WRAPPERS


class BenchmarkBase(benchmark.Benchmark):
    each = 10
    number = 1000
    valid = True

    def __init__(self):
        # Do not run tests using BenchmarkBase itself
        super(BenchmarkBase, self).__init__(BenchmarkBase=False)
        # `validator` variable should be defined in subclasses
        if type(self) != BenchmarkBase:
            self.libraries = WRAPPERS[self.validator]
            # check that validations work as expected
            for library in self.libraries.values():
                assert library.validate(self.data) is self.valid


    def test_marshmallow(self):
        self.__test('marshmallow')

    def test_cerberus(self):
        self.__test('cerberus')

    def __test(self, name):
        library = self.libraries[name]
        for i in range(self.number):
            library.validate(self.data)
