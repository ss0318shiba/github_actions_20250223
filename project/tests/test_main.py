import sys
sys.path.append("~/project")
from unittest import TestCase
from main import function

class MainTestCase(TestCase):
    def test_add(self):
        self.assertEqual(5, function(2, 3))
    def test_add_false(self):
        self.assertEqual(6, function(3, 3))
