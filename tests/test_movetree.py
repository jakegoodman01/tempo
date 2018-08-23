from unittest import TestCase

from tempo import movetree


class MoveTreeNodeTests(TestCase):
    def test_eq(self):
        n1 = movetree.MoveTreeNode('a3')
        n2 = movetree.MoveTreeNode('a3')
        n3 = movetree.MoveTreeNode('b3')
        self.assertEqual(n1 == n2, True)
        self.assertEqual(n1 == n3, False)

    def test_current_square_getter(self):
        n = movetree.MoveTreeNode('b8')
        self.assertEqual(n.current_square, 'b8')

    def test_next_setter_and_getter(self):
        n = movetree.MoveTreeNode('b8')
        n.next = 'a7'
        self.assertEqual(n.next, 'a7')


class MoveTreeHeadTests(TestCase):
    def test_next_getter(self):
        h = movetree.MoveTreeHead('c4')
        self.assertEqual(h.next, set())

        h.add_child('b3')
        h.add_child('d3')
        self.assertEqual(h.next, {'b3', 'd3'})