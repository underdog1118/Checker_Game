'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description: a class shows the game state
'''
from constants import LOW, HIGH, NUM_SQUARES


class GameState:
    '''
        Class -- GameState
            Represents the state of the game.
        Attributes:
            squaures -- the board which shows all pieces positions
            curr_player -- current player
        Methods:
            change_player -- change the current player
            normal_move -- change the squares after a normal move
            cap_move -- change the squares after a capture move
            turn_to_king -- turn the piece into a king
    '''
    def __init__(self):
        '''
            Constructor -- creates an instance of GameState class
            Parameters:
                self -- the current GameState object
        '''
        self.squares = [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
        ]
        self.curr_player = "black"

    def change_player(self, sign):
        '''
            Method -- change_player
                change the player
            Parameter:
                self -- The current GameState object
                sign -- whether to change player
            Returns:
                change "red" to "black" or change "black" to "red"
        '''
        if not sign:
            if self.curr_player == "red":
                self.curr_player = "black"
            else:
                self.curr_player = "red"
        return self.curr_player

    def normal_move(self, prev, next):
        '''
            Method -- normal_move
                Change the squares after a normal move
            Parameter:
                self -- The current GameState object
                next -- The next location, (row, col)
                prev -- The previous location, (row, col)
            Returns:
                Returns new squares.
        '''
        if prev == -1 and next == -1:  # begining status
            return self.squares
        old_loc = self.squares[prev[0]][prev[1]]
        self.squares[next[0]][next[1]] = old_loc
        self.squares[prev[0]][prev[1]] = "empty"
        return self.squares

    def cap_move(self, prev, cap, next):
        '''
            Method -- cap_move
                Change the squares after a capture move
            Parameter:
                self -- The current GameState object
                next -- The next location, (row, col)
                prev -- The previous location, (row, col)
                cap -- The captured location, (row, col)
            Returns:
                Returns new squares.
        '''
        self.squares[next[0]][next[1]] = self.squares[prev[0]][prev[1]]
        self.squares[cap[0]][cap[1]] = "empty"
        self.squares[prev[0]][prev[1]] = "empty"
        return self.squares

    def turn_to_king(self):
        '''
            Method -- turn_to_king
                turn pieces into king pieces, black to king_black,
                red to king_red.
            Parameter:
                self -- The current GameState object
            Returns:
                Returns new squares.
        '''
        for col in range(NUM_SQUARES):
            if self.squares[HIGH][col] == "black":
                self.squares[HIGH][col] = "king_black"
            if self.squares[LOW][col] == "red":
                self.squares[LOW][col] = "king_red"
        return self.squares
