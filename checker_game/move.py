'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description:
'''
from piece import Piece
from constants import SQUARE_SIZE, NUM_SQUARES
import math


class Move:
    '''
        Class -- Move
            Find avaiable normal and capture moves
        Attributes:
            turn -- the current player
            squares -- the current board
            ava_normal_move -- avaiable normal moves list
            ava_cap_move -- avaiable capture moves list
            piece_pos -- the list contains the location of clicked position
        Methods:
            position_converter -- a coordinate conversion function
            get_next_move -- get a single next normal/capture move
            non_king_move -- get avaiable moves of a non_king piece
            king_move -- get avaiable moves of a king piece
            get_nor_moves -- get all avaiable non_king_piece moves on the board
            get_king_moves -- get all avaiable king pieces moves on the board
            get_all_moves -- get all avaiable pieces moves on the board
    '''
    def __init__(self, turn, squares):
        '''
            Constructor -- creates an instance of Move class
            Parameters:
                self -- the current Move object
                turn -- the current player
                squares -- the current board
        '''
        self.turn = turn
        self.squares = squares
        self.ava_normal_move = []
        self.ava_cap_move = []
        self.piece_pos = []

    def position_converter(self, x, y):
        '''
            Method -- position_converter
                convert the original click coordinate to x(0~7) y(0~7) format
            Parameter:
                self -- The current Move object
                x -- x coordinate of clicked position
                y -- y coordinate of clicked position
            Returns:
                a new postion in. [x, y] x and y are integer from 0 - 7
        '''
        col = 4 + math.floor(x / SQUARE_SIZE)
        row = 4 + math.floor(y / SQUARE_SIZE)
        self.piece_pos.append((col, row))
        return self.piece_pos

    def get_next_move(self, x, y, nX, nY, mX, mY):
        '''
            Method -- get_next_mov
                get a single next normal/capture move
            Parameter:
                self -- the current Move object
                x -- x coordinate of clicked position
                y -- y coordinate of clicked position
                nX -- x coordinate of the new position after a normal move
                nY -- y coordinate of the new position after a normal move
                mX -- x coordinate of the new position after a capture move
                my -- y coordinate of the new position after a capture move
            Returns:
                nothing. save avaiable moves in moves lists
        '''
        self.piece = Piece(x, y, self.squares)
        self.oppo = self.piece.get_opponent()  # red / black
        self.color = self.piece.get_color()  # red / black
        self.new_piece = Piece(nX, nY, self.squares)
        self.m_piece = Piece(mX, mY, self.squares)
        if self.new_piece.is_in_boundary() and self.color == self.turn:
            if self.new_piece.get_color() == "empty":
                self.ava_normal_move.append((nX, nY))  # normal move
            if self.m_piece.is_in_boundary() and\
               self.new_piece.get_color() == self.oppo:
                if self.m_piece.get_color() == "empty":
                    self.ava_cap_move.append((mX, mY))  # cap move

    def non_king_move(self, x, y):
        '''
            Method -- normal_move
                get avaiable moves of a non_king piece
            Parameter:
                self -- the current Move object
                x -- x coordinate of the piece
                y -- y coordinate of the piece
            Returns:
                nothing.
        '''
        if self.turn == "black":
            self.get_next_move(x, y, x+1, y+1, x+2, y+2)
            self.get_next_move(x, y, x+1, y-1, x+2, y-2)
        elif self.turn == "red":
            self.get_next_move(x, y, x-1, y+1, x-2, y+2)
            self.get_next_move(x, y, x-1, y-1, x-2, y-2)

    def king_move(self, x, y):
        '''
            Method -- king_move
                get avaiable moves of a king piece
            Parameter:
                self -- the current Move object
                x -- x coordinate of the piece
                y -- y coordinate of the piece
            Returns:
                nothing.
        '''
        self.get_next_move(x, y, x+1, y+1, x+2, y+2)
        self.get_next_move(x, y, x+1, y-1, x+2, y-2)
        self.get_next_move(x, y, x-1, y+1, x-2, y+2)
        self.get_next_move(x, y, x-1, y-1, x-2, y-2)

    def get_nor_moves(self):
        '''
            Method -- get_nor_moves
                get all avaiable non_king_piece moves on the board
            Parameter:
                self -- the current Move object
            Returns:
                nothing.
        '''
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                self.non_king_move(row, col)

    def get_king_moves(self):
        '''
            Method -- get_king_moves
                get all avaiable king pieces moves on the board
            Parameter:
                self -- the current Move object
            Returns:
                nothing.
        '''
        for row in range(NUM_SQUARES):
            for col in range(NUM_SQUARES):
                color = self.squares[row][col]
                if self.turn == "black" and color == "king_black":
                    self.king_move(row, col)
                if self.turn == "red" and color == "king_red":
                    self.king_move(row, col)

    def get_all_moves(self, piece, cap_ls, nor_ls):
        '''
            Method -- get_all_moves
                get all avaiable pieces moves on the board
            Parameter:
                self -- the current Move object
                piece -- the selected piece
                cap_ls -- capture moves of all pieces
                nor_ls -- normal moves of all pieces
            Returns:
                nothing. save available moves in according lists
        '''
        piece.get_nor_moves()
        piece.get_king_moves()
        for move in piece.ava_cap_move:
            cap_ls.append(move)
        for move in piece.ava_normal_move:
            nor_ls.append(move)
