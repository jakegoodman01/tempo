from typing import List


class Board:
    def __init__(self):
        # Rows are called 'ranks' and columns are called 'files'
        # Rows are numbered 1 to 8 and columns are lettered a to h
        self._squares: List[List[str]] = [[f'{file}{i}' for file in 'abcdefgh'] for i in range(1, 9)]

    def get_square_from_notation(self, square: str):
        file = 'abcdefgh'.index(square[0])
        rank = int(square[1]) - 1
        return self._squares[rank][file]

