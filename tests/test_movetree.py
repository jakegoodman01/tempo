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
        self.assertEqual(n.next, movetree.MoveTreeNode('a7'))


class MoveTreeHeadTests(TestCase):
    def test_next_getter(self):
        h = movetree.MoveTreeHead('c4')
        self.assertEqual(h.next, list())

        h.add_child('b3')
        h.add_child('d3')
        self.assertEqual(h.next, ['b3', 'd3'])


class MoveTreeTests(TestCase):
    mt = movetree.MoveTree('d4')
    mt.head.add_child('c3')
    mt.head.add_child('c5')
    mt.head.add_child('e3')
    mt.head.add_child('e5')

    def test_next_square_from_head(self):
        MoveTreeTests.mt.next_square_from_head(2)
        self.assertEqual(MoveTreeTests.mt.token_node, movetree.MoveTreeHead('e3'))

    def test_back_to_head(self):
        MoveTreeTests.mt.back_to_head()
        self.assertEqual(MoveTreeTests.mt.token_node, MoveTreeTests.mt.head)

    def test_next_square(self):
        MoveTreeTests.mt.back_to_head()
        MoveTreeTests.mt.next_square_from_head(1)
        MoveTreeTests.mt.token_node.next = 'b6'
        MoveTreeTests.mt.next_square()
        self.assertEqual(MoveTreeTests.mt.token_node, movetree.MoveTreeNode('b6'))