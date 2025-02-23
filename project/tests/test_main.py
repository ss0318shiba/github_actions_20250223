import sys
sys.path.append("~/work/github_actions_20250223/github_actions_20250223/project/src")
from unittest import TestCase
from main import function

class MainTestCase(TestCase):
    def test_add(self):
        self.assertEqual(5, function(2, 3))
    def test_add_false(self):
        self.assertEqual(6, function(3, 3))
