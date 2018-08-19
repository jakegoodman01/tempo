from enum import Enum


class PieceType(Enum):
    PAWN = 1
    KNIGHT = 3
    BISHOP = 3
    ROOK = 5
    QUEEN = 9
    KING = 999


class Piece:
    def __init__(self, piece_type: PieceType, square: str):
        self.piece_type = piece_type
        self.square = square

