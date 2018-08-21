from enum import Enum


class PieceType(Enum):
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3
    ROOK = 5
    QUEEN = 9
    KING = 999


class Color(Enum):
    WHITE = 1
    BLACK = 1


class Piece:
    def __init__(self, piece_type: PieceType, square: str, color: Color):
        self.piece_type: PieceType = piece_type
        self.square: str = square
        self.color: Color = color

