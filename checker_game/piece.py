'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description: the class represents the state of pieces
'''
import math
from constants import LOW, HIGH


class Piece:
    '''
        Class -- Piece
            get the information and state of a piece
        Attributes:
            row -- the row of a piece
            col -- the col of a piece
            squares -- the state of the board
        Methods:
            get_color -- get the color of the piece
            is_in_boundary -- checks whether the piece is in the bound
            get_opponent -- get the oppoent of the piece
            check_king -- check whether the piece is a king
    '''
    def __init__(self, row, col, square):
        '''
            Constructor to create an instance of Piece class.
            Parameters:
                row -- An int that represents the row of a piece.
                col --  An int that represents the column of a piece.
                square -- The state of the board.
        '''
        self.row = row
        self.col = col
        self.square = square

    def get_color(self):
        '''
            Method -- get_color
                get the color of a piece, black or red
            Parameter:
                self -- The current piece object
            Returns:
                the color of the piece
        '''
        if self.square[self.row][self.col] == "king_black":
            return "black"
        if self.square[self.row][self.col] == "king_red":
            return "red"
        return self.square[self.row][self.col]

    def is_in_boundary(self):
        '''
            Method -- is_in_boundary
                check whether the clickde position is in bound
            Parameter:
                self -- The current piece object
            Returns:
                return true if it's in bound, else return false
        '''
        return self.row >= LOW and self.row <= HIGH\
            and self.col >= LOW and self.col <= HIGH

    def get_opponent(self):
        '''
            Method -- get_opponent
                get the opponent color of a piece
            Parameter:
                self -- The current piece object
            Returns:
                if the piece is black or king_black, return red;
                if the piece is red or king_red, return black
        '''
        if self.get_color() == "black" or self.get_color() == "king_black":
            return "red"
        elif self.get_color() == "red" or self.get_color() == "red_king":
            return "black"
        else:
            return None

    def check_king(self):
        '''
            Method -- check_king
                check whether the piece is a king
            Parameter:
                self -- The current piece object
            Returns:
                if the piece is king_black or king_red, return true,
                else return false
        '''
        x = self.row
        y = self.col
        return self.square[x][y] == "king_black" or\
            self.square[x][y] == "king_red"
