import unittest
from .. import translator

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_None(self):
        with self.assertRaises(ValueError) as exception_context:
            englishToFrench(None)
        self.assertEqual(
            str(exception_context.exception),
            "text must be provided"
        )

    def test_frenchToEnglish_None(self):
        with self.assertRaises(ValueError) as exception_context:
            frenchToEnglish(None)
        self.assertEqual(
            str(exception_context.exception),
            "text must be provided"
        )

    def test_englishToFrench_Hello(self):
        self.assertEqual(
            englishToFrench('Hello'),
            'Bonjour'
        )

    def test_englishToFrench_Bonjour(self):
        self.assertEqual(
            englishToFrench('Bonjour'),
            'Bonjour'
        )

    def test_frenchToEnglish_Bonjour(self):
        self.assertEqual(
            frenchToEnglish('Bonjour'),
            'Hello'
        )

    def test_frenchToEnglish_Hello(self):
        self.assertEqual(
            frenchToEnglish('Hello'),
            'Hello'
        )

if __name__ == "__main__":
    unittest.main()