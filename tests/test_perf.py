from unittest import TestCase
try:
    from unittest import mock
except ImportError:
    from mock import mock


class TestResults(TestCase):
    def test_simple(self):
        self.assertEqual(0, 1)
