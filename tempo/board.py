class Board:
    def __init__(self):
        # Rows are called 'ranks' and columns are called 'files'
        # Rows are numbered 1 to 8 and columns are lettered a to h
        self._squares = [[f'{file}{i}' for file in 'abcdefgh'] for i in range(1, 9)]