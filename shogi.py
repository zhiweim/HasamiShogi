# Author: Zhiwei Ma
# Date: 11/20/21
# Description: Hasami Shogi Game

class HasamiShogiGame:
    """
    Hasami Shogi Game
    """
    def __init__(self):
        """
        Initializes the board and sets the game state to 'UNFINISHED' and the current active player to be 'BLACK'
        Also initializes the number of red and black captured pieces to both be 0.
        """
        self._game_state = 'UNFINISHED'
        self._active_player = 'BLACK'
        self._red_captured = 0
        self._black_captured = 0
        self._board = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                       ['a', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'],
                       ['b', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['c', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['d', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['e', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['f', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['g', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['h', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                       ['i', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]

    def print_board(self):
        """
        prints the board in a more readable fashion
        """
        for s in self._board:
            print(*s)

    def make_move(self, first, last):
        """
        Takes in two parameters that goes through another method that converts them into integers. Checks for several
        conditions to ensure that the move being made is a valid one. At the end of each successful make_move call,
        set_next_active_player is called so that it is the other players turn. A capture_helper method is called
        after each player's make_move is called successfully and checks for several conditions if pieces are captured.
        If any player's piece has 8 or more captured pieces the game state is set to the player's win
        """
        x, y = self._convert(first)  # converts the first move to a tuple
        i, j = self._convert(last)  # converts the second move to a tuple
        if x != i and y != j:  # if an illegal movement is made
            return False
        if self._board[i][j] != '.':
            return False
        if self._game_state != 'UNFINISHED' or self._red_captured >= 8 or self._black_captured >= 8:
            return False
        if self._board[x][y] == 'B' and self.get_active_player() == 'BLACK' and self.get_game_state() == 'UNFINISHED':
            if self._move_valid(x, y, i, j):
                self._board[i][j] = self._board[x][y]
                self._board[x][y] = '.'
                self._set_next_active_player()
                self._black_capture_helper(i, j)
                if self._red_captured >= 8:
                    self._set_game_state_black()
                return True
            else:
                return False
        elif self._board[x][y] == 'R' and self.get_active_player() == 'RED' and self.get_game_state() == 'UNFINISHED':
            if self._move_valid(x, y, i, j):
                self._board[i][j] = self._board[x][y]
                self._board[x][y] = '.'
                self._set_next_active_player()
                self._red_capture_helper(i, j)
                if self._black_captured >= 8:
                    self._set_game_state_red()
                return True
            else:
                return False
        else:
            return False

    def _move_valid(self, x, y, i, j):
        """
        return True if move is valid and updates board, otherwise return false if final
        destination is not valid such as encountering any pieces at all before moving to final destination
        """
        c = 1
        if x == i:  # if the final position is in the same index
            if y < j:  # moving from left to right on same list
                while self._board[x][y+c] == '.':
                    y += c
                    if y == j:
                        return True
                else:
                    return False
            elif j < y:  # moving from right to left on same list
                while self._board[x][y-c] == '.':
                    y -= c
                    if y == j:
                        return True
                else:
                    return False
        elif y == j:  # if the final position is in the same list
            if x < i:
                while self._board[x+c][y] == '.':
                    x += c
                    if x == i:
                        return True
                else:
                    return False
            elif x > i:
                while self._board[x-c][y] == '.':
                    x -= c
                    if x == i:
                        return True
                else:
                    return False
        else:  # if the final position is neither in the same list nor index
            return False

    def _red_capture_helper(self, i, j):
        """
        At the end of make_move, the piece should scan all four directions and if a RED piece is encountered,
        keep looping until it encounters either 'B', or '.'
        Also checks for corner pieces if the final position can potentially capture a corner piece
        """
        c = 1
        num = 0
        v = i
        h = j

        if i == 1 and j == 2:  # corner piece captures
            if self._board[1][1] == 'B' and self._board[2][1] == 'R':
                self._board[1][1] = '.'
                self._black_captured += 1

        if i == 2 and j == 1:
            if self._board[1][1] == 'B' and self._board[1][2] == 'R':
                self._board[1][1] = '.'
                self._black_captured += 1

        if i == 1 and j == 8:
            if self._board[1][9] == 'B' and self._board[2][9] == 'R':
                self._board[1][9] = '.'
                self._black_captured += 1

        if i == 2 and j == 9:
            if self._board[1][9] == 'B' and self._board[1][8] == 'R':
                self._board[1][9] = '.'
                self._black_captured += 1

        if i == 8 and j == 1:
            if self._board[9][1] == 'B' and self._board[9][2] == 'R':
                self._board[9][1] = '.'
                self._black_captured += 1

        if i == 9 and j == 2:
            if self._board[9][1] == 'B' and self._board[8][1] == 'R':
                self._board[9][1] = '.'
                self._black_captured += 1

        if i == 8 and j == 9:
            if self._board[9][9] == 'B' and self._board[9][8] == 'R':
                self._board[9][9] = '.'
                self._black_captured += 1

        if i == 9 and j == 8:
            if self._board[9][9] == 'B' and self._board[8][9] == 'R':
                self._board[9][9] = '.'
                self._black_captured += 1

        if j < 9:
            while self._board[i][j+c] == 'B':  # checking right of board ; error if list is out of range
                j += c
                num += 1
                if j == 9:
                    break
                if self._board[i][j+c] == 'R':
                    self._black_captured += num
                    while j != h:
                        self._board[i][j] = '.'
                        j -= c
        if j > 1:
            j = h
            i = v
            while self._board[i][j-c] == 'B':  # checking left of board
                j -= c
                num += 1
                if j == 1:
                    break
                if self._board[i][j-c] == 'R':
                    self._black_captured += num
                    while j != h:
                        self._board[i][j] = '.'
                        j += c
        if i < 9:
            j = h
            i = v
            while self._board[i+c][j] == 'B':  # checking below board
                i += c
                num += 1
                if i == 9:
                    break
                if self._board[i+c][j] == 'R':  # encountering another B piece
                    self._black_captured += num  # captures the number of red pieces
                    while i != v:
                        self._board[i][j] = '.'
                        i -= c
        if i > 1:
            j = h
            i = v
            while self._board[i-c][j] == 'B':  # checking above board
                i -= c
                num += 1
                if i == 1:
                    break
                if self._board[i-c][j] == 'R':
                    self._black_captured += num
                    while i != v:
                        self._board[i][j] = '.'
                        i += c

    def _black_capture_helper(self, i, j):
        """
        At the end of make_move, the piece should scan all four directions and if a RED piece is encountered,
        keep looping until it encounters either 'B', or '.'
        Also checks for corner pieces if the final position can potentially capture a corner piece
        """
        c = 1
        num = 0
        v = i
        h = j

        if i == 1 and j == 2:  # corner piece captures
            if self._board[1][1] == 'R' and self._board[2][1] == 'B':
                self._board[1][1] = '.'
                self._red_captured += 1

        if i == 2 and j == 1:
            if self._board[1][1] == 'R' and self._board[1][2] == 'B':
                self._board[1][1] = '.'
                self._red_captured += 1

        if i == 1 and j == 8:
            if self._board[1][9] == 'R' and self._board[2][9] == 'B':
                self._board[1][9] = '.'
                self._red_captured += 1

        if i == 2 and j == 9:
            if self._board[1][9] == 'R' and self._board[1][8] == 'B':
                self._board[1][9] = '.'
                self._red_captured += 1

        if i == 8 and j == 1:
            if self._board[9][1] == 'R' and self._board[9][2] == 'B':
                self._board[9][1] = '.'
                self._red_captured += 1

        if i == 9 and j == 2:
            if self._board[9][1] == 'R' and self._board[8][1] == 'B':
                self._board[9][1] = '.'
                self._red_captured += 1

        if i == 8 and j == 9:
            if self._board[9][9] == 'R' and self._board[9][8] == 'B':
                self._board[9][9] = '.'
                self._red_captured += 1

        if i == 9 and j == 8:
            if self._board[9][9] == 'R' and self._board[8][9] == 'B':
                self._board[9][9] = '.'
                self._red_captured += 1

        if j < 9:
            v = i
            h = j
            while self._board[i][j+c] == 'R':  # checking right of board
                j += c
                num += 1
                if j == 9:
                    break
                if self._board[i][j+c] == 'B':
                    self._red_captured += num
                    while j != h:
                        self._board[i][j] = '.'
                        j -= c
        if j > 1:
            j = h
            i = v
            while self._board[i][j-c] == 'R':  # checking left of board
                j -= c
                num += 1
                if j == 1:
                    break
                if self._board[i][j-c] == 'B':
                    self._red_captured += num
                    while j != h:
                        self._board[i][j] = '.'
                        j += c
        if i < 9:
            j = h
            i = v
            while self._board[i+c][j] == 'R':  # checking below board
                i += c
                num += 1
                if i == 9:
                    break
                if self._board[i+c][j] == 'B':  # encountering another B piece
                    self._red_captured += num  # captures the number of red pieces
                    while i != v:
                        self._board[i][j] = '.'
                        i -= c
        if i > 1:
            j = h
            i = v
            while self._board[i-c][j] == 'R':  # checking above board
                i -= c
                num += 1
                if i == 1:
                    break
                if self._board[i-c][j] == 'B':
                    self._red_captured += num
                    while i != v:
                        self._board[i][j] = '.'
                        i += c

    def get_game_state(self):
        """
        returns the game state
        """
        return self._game_state

    def get_active_player(self):
        """
        returns the current active player
        """
        return self._active_player

    def get_num_captured_pieces(self, color):
        """
        Takes in a color parameter and returns the number of captured pieces
        """
        if color == 'RED':
            return self._red_captured
        elif color == 'BLACK':
            return self._black_captured
        else:
            return 'Not a valid color!'

    def get_square_occupant(self, square):
        """
        Takes in the board's square as a parameter and returns whatever is occupying it
        """
        x, y = self._convert(square)
        if self._board[x][y] == 'B':
            return 'BLACK'
        elif self._board[x][y] == 'R':
            return 'RED'
        else:
            return 'NONE'

    def _set_game_state_red(self):
        """
        sets the game state to 'RED_WON'
        """
        self._game_state = 'RED_WON'

    def _set_game_state_black(self):
        """
        Sets the game state to 'BLACK_WON'
        """
        self._game_state = 'BLACK_WON'

    def _set_next_active_player(self):
        """
        After make_move is called successfully, sets the the active player to be the opposite color
        """
        if self.get_active_player() == 'BLACK':
            self._active_player = 'RED'
        else:
            self._active_player = 'BLACK'

    def _convert(self, sq):
        """
        Converts make_move parameters into integers
        """
        x, y = sq
        if x == 'a':
            y = int(y)
            x = 1
            return x, y
        if x == 'b':
            y = int(y)
            x = 2
            return x, y
        if x == 'c':
            y = int(y)
            x = 3
            return x, y
        if x == 'd':
            y = int(y)
            x = 4
            return x, y
        if x == 'e':
            y = int(y)
            x = 5
            return x, y
        if x == 'f':
            y = int(y)
            x = 6
            return x, y
        if x == 'g':
            y = int(y)
            x = 7
            return x, y
        if x == 'h':
            y = int(y)
            x = 8
            return x, y
        if x == 'i':
            y = int(y)
            x = 9
            return x, y
        else:
            return False



