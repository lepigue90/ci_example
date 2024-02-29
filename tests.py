"""Necessary Docstring added to pass linter"""
import unittest
import task


class TestCase(unittest.TestCase):
    """Necessary doctring added to pass linter"""

    def test1(self):
        """Necessary docstring added to pass linter"""
        expected = "Hello World"
        self.assertEqual(task.my_func(), expected)

    def test2(self):
        """Necessary docstring added to pass linter"""
        expected = "Hola World"
        self.assertNotEqual(task.my_func(), expected)


if __name__ == '__main__':
    unittest.main()
