import unittest

from utils import sample

class TestSample(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(sample("World"), "Hello World!")