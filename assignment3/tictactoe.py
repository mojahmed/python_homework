#Task 6 

class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines = []
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} \n")
        lines.append("-----------\n")
        lines.append(f" {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} \n")
        return "".join(lines)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        index = Board.valid_moves.index(move_string)
        row = index // 3
        col = index % 3

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = (row, col)

        # Switch turn
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check win rows
        for row in self.board_array:
            if row[0] != " " and row[0] == row[1] == row[2]:
                return (True, f"{row[0]} wins!")

        # Check win columns
        for col in range(3):
            if self.board_array[0][col] != " " and self.board_array[0][col] == self.board_array[1][col] == self.board_array[2][col]:
                return (True, f"{self.board_array[0][col]} wins!")

        # Check diagonals
        if self.board_array[1][1] != " ":
            if self.board_array[0][0] == self.board_array[1][1] == self.board_array[2][2]:
                return (True, f"{self.board_array[1][1]} wins!")
            if self.board_array[0][2] == self.board_array[1][1] == self.board_array[2][0]:
                return (True, f"{self.board_array[1][1]} wins!")

        # Check for tie
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game.")

        # Game not over
        return (False, f"{self.turn}'s turn.")

# --- Game runner ---
if __name__ == "__main__":
    board = Board()
    print("Welcome to TicTacToe!")
    while True:
        print(board)
        status, message = board.whats_next()
        if status:
            print(message)
            break
        try:
            move_input = input(f"{board.turn}'s move: ").strip()
            board.move(move_input)
        except TictactoeException as e:
            print("Error:", e.message)
