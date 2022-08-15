class TicTacToe:
    def __int__(self):
        self.board = [" " for _ in range(9)]  # we are using a single list to represent 3x3 board
        self.current_winner = None  # keep track of winner!
        