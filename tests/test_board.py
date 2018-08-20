from unittest import TestCase

from tempo import Board


class BoardTests(TestCase):
    def test_validate_square(self):
        self.assertEqual(Board.validate_square('a3'), True)
        self.assertEqual(Board.validate_square('13'), False)
        self.assertEqual(Board.validate_square('h9'), False)