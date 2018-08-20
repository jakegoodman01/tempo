from unittest import TestCase

from tempo import Board


class BoardTests(TestCase):
    def test_get_square_from_notation(self):
        b = Board()
        self.assertEqual(b.get_square_from_notation('a3'), 'a3')
        self.assertEqual(b.get_square_from_notation('c6'), 'c6')