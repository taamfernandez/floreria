import unittest
from prueba import eliminar

class TestProbar(unittest.TestCase):
    def test_eliminar(self):
        self.assertEqual(eliminar('4')True)
