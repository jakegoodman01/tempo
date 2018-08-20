from typing import List


class Board:
    def __init__(self):
        # Rows are called 'ranks' and columns are called 'files'
        # Rows are numbered 1 to 8 and columns are lettered a to h
        self._squares: List[List[str]] = [[f'{file}{i}' for file in 'abcdefgh'] for i in range(1, 9)]

    @classmethod
    def validate_square(cls, square: str) -> bool:
        return square[0] in 'abcdefgh' and square[1] in '12345678'


