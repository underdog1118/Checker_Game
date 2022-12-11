'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description: Checkers main function
'''
import turtle
import math
import time
from game_state import GameState
from function import Function
from piece import Piece
from move import Move
from random import choice
from constants import SQUARE_SIZE, NUM_SQUARES, ABS_MAX_BOUNDS


class Perform:
    '''
        Class -- Perform
            Run the game
        Attributes:
            square_colors -- the colors list
            pos_lst -- the possible location in the board (0-7)
            pos -- temporary position storage
            old_pos -- old position
            pos_to_move -- new position
            ava_nor_move -- one piece normal moves
            ava_cap_move -- one piece cap moves
            is_cap_ava -- all pieces cap moves
            is_nor_ava -- all pieces normal moves
            choose_piece -- the boolean sign whether move to the second click
            captured -- the boolean sign whether execute multiple capture moves
            legal_move -- the boolean sign whether the move is a legal one
            pen -- a tool in turtle library
            squares -- the default board
            turn -- current player
            game_state -- an instance of GameState class
            draw -- an instance of Function class
            screen -- the function in turtle of click detection
        Methods:
            position_converter -- convert the clicked position to (0~7) format
            click_handler -- detect new click event
            first_click -- check whether the first click is a valid piece
                           and check it's available moves and show
            second_click -- check if the second click is valid, if it is,
                        check it is a normal move or a capture move, if it's
                        a capture move, check multiple capture moves. Then
                        update the board after move.
            ai_move -- computer player move (red)
            board_update -- update the board UI after each move
            clear_all_move -- clear all moves lists
            random_pick -- ai randomly pick an available move to execute
            check_game_over -- check if one player wins and game over
    '''
    def __init__(self):
        '''
            Constructor -- creates an instance of Perform class
            Parameters:
                self -- the current Perform object
        '''
        self.square_colors = ("light gray", "white", "red", "black",
                              "deep sky blue", "orange red")
        self.pos_lst = [0, 1, 2, 3, 4, 5, 6, 7]
        self.pos = []  # temporary position storage
        self.old_pos = []  # old position
        self.pos_to_move = []   # new position
        self.ava_nor_move = []  # one piece normal moves
        self.ava_cap_move = []  # one piece cap moves
        self.is_cap_ava = []  # all pieces cap moves
        self.is_nor_ava = []  # all pieces normal moves
        self.choose_piece = True
        self.captured = False
        self.legal_move = True

        self.pen = turtle.Turtle()  # This variable does the drawing.
        self.pen.penup()  # This allows the pen to be moved.
        self.pen.hideturtle()  # This gets rid of the triangle cursor.
        # The first parameter is the outline color, the second is the fille
        self.game_state = GameState()
        self.squares = self.game_state.normal_move(-1, -1)
        self.turn = self.game_state.curr_player
        print("Your turn: " + self.turn)
        self.draw = Function(self.pen, SQUARE_SIZE, self.square_colors,
                             NUM_SQUARES)
        self.draw.draw_board()
        self.draw.draw_pieces(self.squares)

        # Click handling
        screen = turtle.Screen()
        # This will call call the click_handler function when a click occurs
        screen.onclick(self.click_handler)
        # turtle.done()  # Stops the window from closing.
        turtle.done()

    def position_converter(self, x, y):
        '''
            Method -- position_converter
                convert the original click coordinate to x(0~7) y(0~7) format
            Parameter:
                self -- The current Move object
                x -- x coordinate of clicked position
                y -- y coordinate of clicked position
            Returns:
                a new postion. [x, y] x and y are integer from 0 - 7
        '''
        col = 4 + math.floor(x / SQUARE_SIZE)
        row = 4 + math.floor(y / SQUARE_SIZE)
        return row, col

    def click_handler(self, x, y):
        '''
            Method -- click_handler
                Called when a click occurs.
            Parameters:
                self -- the current Perform object
                x -- X coordinate of the click. Automatically provided
                y -- Y coordinate of the click. Automatically provided
            Returns:
                Does not and should not return. Click handlers are a special
                of function automatically called by Turtle. You will not have
                access to anything returned by this function.
        '''
        print("--------new move--------")
        print("Your turn : " + self.turn)
        self.pos = self.position_converter(x, y)  # [row, col]
        self.piece = Move(self.turn, self.squares)
        self.piece.get_all_moves(self.piece, self.is_cap_ava, self.is_nor_ava)
        if abs(x) > ABS_MAX_BOUNDS or abs(y) > ABS_MAX_BOUNDS:
            print("Out of bounds !")
        else:
            self.color = self.squares[self.pos[0]][self.pos[1]]
            print("Clicked at [", self.pos, "] : " + self.color)
            x = self.pos[0]
            y = self.pos[1]
            if self.choose_piece:
                self.first_click(x, y)
            else:
                self.second_click(x, y)
            if self.turn == self.square_colors[2]:  # red ai round
                self.ai_move()
                time.sleep(0.75)

    def first_click(self, x, y):
        '''
            Method -- first_click
                check whether the first click is a valid piece and
                check it's available moves and show them
            Parameters:
                self -- the current Perform object
                x -- X coordinate of the click.
                y -- Y coordinate of the click.
            Returns:
                Nothing. if the first click is valid, move to second
                click, else repeat first click
        '''
        self.chosed_piece = (x, y)
        row = self.chosed_piece[0]
        col = self.chosed_piece[1]
        self.old_pos = (row, col)
        self.n_move = Move(self.turn, self.squares)
        self.k_piece = Piece(row, col, self.squares)
        if self.k_piece.check_king():
            self.n_move.king_move(row, col)
        else:
            self.n_move.non_king_move(row, col)

        if self.n_move.ava_normal_move == [] and\
           self.n_move.ava_cap_move == [] and self.turn == "black" \
           and self.legal_move:
            print("Please select a movable piece !")
        elif not self.legal_move:
            print("Please make a legal move !")
            self.legal_move = True
        else:
            self.ava_cap_move = []
            if self.turn == "black":
                print("The piece can move to: " +
                      str(self.n_move.ava_normal_move))
                print("The piece can capture and move to: " +
                      str(self.n_move.ava_cap_move))
            for move in self.n_move.ava_normal_move:
                self.ava_nor_move.append(move)
            for move in self.n_move.ava_cap_move:
                self.ava_cap_move.append(move)

            # draw seleted piece and possible moves shadow
            if self.turn == "black":
                self.draw.draw_shadow(row, col, self.square_colors[4])
                self.all_moves = self.ava_nor_move + self.ava_cap_move
                for loc in self.all_moves:
                    x = loc[0]
                    y = loc[1]
                    self.draw.draw_shadow(x, y, self.square_colors[5])
            self.choose_piece = False  # move to second click

    def second_click(self, x, y):
        '''
            Method -- second_click
                check if the second click is valid, if it is,
                check it is a normal move or a capture move, if it's
                a capture move, check multiple capture moves. Then
                update the board after move.
            Parameters:
                self -- the current Perform object
                x -- X coordinate of the click.
                y -- Y coordinate of the click.
            Returns:
                Nothing.
        '''
        self.moving_piece = (x, y)  # [row, col]
        row = self.moving_piece[0]
        col = self.moving_piece[1]
        self.pos_to_move = (row, col)
        self.new_piece = Piece(row, col, self.squares)
        cap_row = int((self.moving_piece[0] + self.chosed_piece[0]) / 2)
        cap_col = int((self.moving_piece[1] + self.chosed_piece[1]) / 2)
        self.cap_piece = (cap_row, cap_col)

        if self.is_cap_ava != [] and\
           (self.pos_to_move not in self.is_cap_ava or
           self.ava_cap_move == []):
            print("You must make a capturing move !")
            self.draw.clear_shadow(self.square_colors[3])
            self.choose_piece = True
            self.clear_all_moves()
            return
        elif self.pos_to_move in self.ava_cap_move:  # capture move
            self.squares =\
                self.game_state.cap_move(self.old_pos, self.cap_piece,
                                         self.pos_to_move)
            # multiply cap
            self.game_state.turn_to_king()  # turn to king then multiply move
            self.ava_cap_move = []
            self.multi = Move(self.turn, self.squares)
            # self.multi.ava_cap_move = []
            self.k_piece = Piece(row, col, self.squares)
            if self.k_piece.check_king():
                self.multi.king_move(row, col)
            else:
                self.multi.non_king_move(row, col)
            if self.multi.ava_cap_move != []:
                self.captured = True
            else:
                self.captured = False
            self.clear_all_moves()
            self.board_update()
            return
        elif self.pos_to_move in self.ava_nor_move:  # normal move
            self.squares =\
                self.game_state.normal_move(self.old_pos, self.pos_to_move)
            self.captured = False  # change player
            self.ava_nor_move = []
            self.is_nor_ava = []
            self.board_update()
            return
        else:
            self.choose_piece = True
            self.ava_cap_move = []
            self.ava_nor_move = []
            self.draw.clear_shadow(self.square_colors[3])
            self.legal_move = False
            self.first_click(x, y)
            return

    def ai_move(self):
        '''
            Method -- ai_move
                computer player move as a red piece
            Parameters:
                self -- the current Perform object
            Returns:
                Nothing.
        '''
        ai_turn = True
        while ai_turn:
            self.ai_piece = Move(self.turn, self.squares)
            self.ai_piece.get_all_moves(self.piece, self.is_cap_ava,
                                        self.is_nor_ava)
            while True:
                row = choice(self.pos_lst)  # random pick
                col = choice(self.pos_lst)
                if (self.squares[row][col] == "red" or
                    self.squares[row][col] == "king_red") and\
                   self.turn == "red":

                    self.first_click(row, col)
                    if self.is_cap_ava != [] and self.ava_cap_move == []:
                        continue
                    elif self.ava_cap_move != []:  # ai cap move
                        new_row, new_col = self.random_pick(self.ava_cap_move)
                        self.second_click(new_row, new_col)
                        while self.captured is True:  # ai multi cap, still red
                            time.sleep(1)
                            self.first_click(new_row, new_col)
                            new_row, new_col =\
                                self.random_pick(self.ava_cap_move)
                            self.second_click(new_row, new_col)
                    elif self.ava_nor_move != []:  # ai normal move
                        new_row, new_col =\
                             self.random_pick(self.ava_nor_move)
                        self.second_click(new_row, new_col)
                    break
            if self.turn == self.square_colors[3]:  # black player turn
                ai_turn = False

    def board_update(self):
        '''
            Method -- board_update
                update the board UI after each move
            Parameters:
                self -- the current Perform object
            Returns:
                Nothing.
        '''
        self.game_state.turn_to_king()
        self.turn = self.game_state.change_player(self.captured)
        self.choose_piece = True
        self.check_game_over()
        self.draw.draw_board()
        self.draw.draw_pieces(self.squares)

    def clear_all_moves(self):
        '''
            Method -- clear_all_moves
                clear all moves lists
            Parameters:
                self -- the current Perform object
            Returns:
                Nothing.
        '''
        self.ava_cap_move = []
        self.ava_nor_move = []
        self.is_cap_ava = []
        self.is_nor_ava = []

    def random_pick(self, lst):
        '''
            Method -- random_pick
                ai randomly pick an available move
            Parameters:
                self -- the current Perform object
                lst -- all possible moves. a list
            Returns:
                return the picked piece position. (row, col)
        '''
        new_piece = choice(lst)
        new_row = new_piece[0]
        new_col = new_piece[1]
        return new_row, new_col

    def check_game_over(self):
        '''
            Method -- check_game_over
                check if one player wins and game over.
            Parameters:
                self -- the current Perform object
            Returns:
                If the game is over, print the winner turn and
                quit the game, else continue the game
        '''
        self.piece = Move(self.turn, self.squares)
        self.piece.get_all_moves(self.piece, self.is_cap_ava, self.is_nor_ava)
        if self.is_cap_ava == [] and self.is_nor_ava == []:
            if self.turn == "black":
                winner = "red"
            elif self.turn == "red":
                winner = "black"
            print("Game over , " + winner + " won!")
            quit()
        else:
            self.is_cap_ava = []
            self.is_nor_ava = []
