import unittest
import parser


class ParserTests(unittest.TestCase):

    def setUp(self):
        self.example_parsed_file = parser.SwiftFileParser(
            file="resources/ExampleFile.swift",
            base_path=""
        ).parse()

    def test_swiftparser_parse_should_return_expected_framework_name(self):
        self.assertEqual(self.example_parsed_file.framework_name, "resources")

    def test_swiftparser_parse_should_return_expected_imports(self):
        self.assertEqual(self.example_parsed_file.imports, ['Foundation', 'AmazingFramework'])

    def test_swiftparser_parse_should_return_expected_interfaces(self):
        self.assertEqual(self.example_parsed_file.interfaces, ["SimpleProtocol {}"])

    def test_swiftparser_parse_should_return_expected_concretes(self):
        self.assertEqual(self.example_parsed_file.concretes, ['GenericStruct<T> {',
                                                              'InternalStruct {}',
                                                              'SimpleClass: SimpleProtocol {',
                                                              'ComplexClass: SimpleClass {',
                                                              'ComposedAttributedClass {}'])

    def test_swiftparser_parse_should_return_expected_methods(self):
        self.assertEqual(self.example_parsed_file.methods, ['methodOne() {',
                                                            'methodTwo(with param1: Int, param2: Int) -> Int {',
                                                            'aStaticMethod() {'])


    def test_swiftparser_parse_should_return_expected_n_of_comments(self):
        self.assertEqual(self.example_parsed_file.n_of_comments, 20)

    def test_swiftparser_parse_should_return_expected_loc(self):
        self.assertEqual(self.example_parsed_file.loc, 21)


if __name__ == '__main__':
    unittest.main()
