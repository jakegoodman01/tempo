from tempo import Board

from typing import List


class MoveTreeNode:
    """See MoveTree class for description"""

    def __init__(self, current_square: str):
        self._current_square: str = current_square
        self._next: str = None

    def __eq__(self, other):
        return isinstance(other, MoveTreeNode) and self._current_square == other._current_square

    @property
    def current_square(self):
        return self._current_square

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value: str):
        if Board.validate_square(value):
            self._next = value
        else:
            raise ValueError('Invalid square')


class MoveTreeHead(MoveTreeNode):
    """This is the head node of a MoveTree. The difference between MoveTreeHead and MoveTreeNode is that MoveTreeHead
    can have multiple 'next' values but MoveTreeNodes only have one 'next' value"""

    def __init__(self, current_square: str):
        super().__init__(current_square)
        del super()._next
        self._next: List[str] = []

    @property
    def next(self):
        return self._next


class MoveTree:
    """A MoveTree is a tree where each node is a square on a chess board. The head of the MoveTree is the starting
    square of a Piece. Each node's parent is the square that the piece would have come from, and each node's
    child/children are the squares it could possibly go to. Each node is a MoveTreeNode. Since all chess pieces only
    move in a linear fashion, a MoveTree is essentially a head node with a number of linked lists branching from it.
    """

    def __init__(self, head: str):
        self.head: MoveTreeHead = MoveTreeHead(head)
        self.token_node: MoveTreeNode = self.head  # when moving through the MoveTree, token_node is the current node

    def back_to_head(self):
        self.token_node = self.head

    def next_square(self):
        if self.token_node == self.head:
            raise RuntimeError('There is no obvious next square. Use next_square_from_head')
        self.token_node = self.token_node.next

    def next_square_from_head(self, index):
        if self.token_node != self.head:
            raise RuntimeError('token_node must be the head of this MoveTree to use next_square_from_head')
        self.token_node = self.token_node.next[index]