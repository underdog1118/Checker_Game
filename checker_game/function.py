'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description: a class which contains drawing functions,
including draw board, pieces and shadows
'''

import turtle
from piece import Piece


class Function:
    '''
        Class -- Function
            draw board, pieces and shadows
        Attributes:
            pen -- a turtle function
            square_size -- the size of a square of the board
            square_colors -- the color of squares
            num_squares -- the number of squares of the board
            board_size -- the area of the board
            cornor -- the location of lower left corner of the board
        Methods:
            draw_square -- draws a square
            draw_circle -- draws a circle
            draw_empty_square -- draw a hollow square
            draw_board -- draws a board
            draw_pieces -- draws pieces
            draw_shadow -- draw the shadow of a selected piece
            clear_shadow -- clear all shadows
    '''
    def __init__(self, turtle, square_size, square_colors, num_squares):
        '''
            Constructor to create an instance of Function class.
            Parameters:
                turtle -- a draw function
                square_size -- the size of a square of the board
                square_colors -- the color of squares
                num_squares -- the number of squares of the board
        '''
        self.pen = turtle
        self.square_size = square_size
        self.square_colors = square_colors
        self.num_squares = num_squares
        self.board_size = self.num_squares * self.square_size
        self.cornor = - self.board_size / 2 + 1

    def draw_square(self, size):
        '''
            Method -- draw_square
                Draw a square with a certain size
            Parameters:
                self -- an instance of Turtle
                size -- the length of each side of the square
            Returns:
                Nothing. Draws a square in the graphics window.
        '''
        RIGHT_ANGLE = 90
        LINES = 4
        self.pen.begin_fill()
        self.pen.pendown()
        for i in range(LINES):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.end_fill()
        self.pen.penup()

    def draw_circle(self, size, color):
        '''
            Method -- draw_circle
                Draw a circle with a given radius.
            Parameters:
                self -- an instance of Turtle
                size -- the radius of the circle
                color -- the color of circle
            Returns:
                Nothing. Draws a circle in the graphics windo.
        '''
        self.pen.pendown()
        self.pen.pencolor(color)
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        self.pen.circle(size)
        self.pen.end_fill()
        self.pen.penup()

    def draw_empty_square(self, size):
        '''
            Method -- draw_empty_square
                Draw a hollow square of a given size.
            Parameters:
                self -- an instance of Turtle
                size -- the length of each side of the square
            Returns:
                Nothing. Draws a hollow square in the graphics window.
        '''
        RIGHT_ANGLE = 90
        LINES = 4
        self.pen.pendown()
        for i in range(LINES):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.penup()

    def draw_board(self):
        '''
            Method -- draw_board
                Draw a board
            Parameters:
                self -- an instance of Turtle
            Returns:
                Nothing. Draws a board
        '''
        # Create the UI window. This should be the width of the board plus a
        # little margin
        window_size = self.board_size + self.square_size
        turtle.setup(window_size, window_size)

        # Set the drawing canvas size. The should be actual board size
        turtle.screensize(self.board_size, self.board_size)
        turtle.bgcolor("white")  # The window's background color
        turtle.tracer(0, 0)  # makes the drawing appear immediately

        self.pen = turtle.Turtle()  # This variable does the drawing.
        self.pen.penup()  # This allows the pen to be moved.
        self.pen.hideturtle()  # This gets rid of the triangle cursor.

        # The first parameter is the outline color, the second is the fille
        self.pen.color("black", "white")
        self.pen.setposition(self.cornor, self.cornor)
        self.draw_square(self.board_size)
        self.pen.color("black", self.square_colors[0])
        for col in range(self.num_squares):
            for row in range(self.num_squares):
                if row % 2 != col % 2:
                    self.pen.setposition(self.cornor + self.square_size * col,
                                         self.cornor + self.square_size * row)
                    self.draw_square(self.square_size)

    def draw_pieces(self, location):
        '''
            Method -- draw_pieces
                Draw all pieces in the board
            Parameters:
                self -- an instance of Turtle
                location -- the x,y position of pieces
            Returns:
                Nothing. Draws pieces
        '''
        for row in range(len(location)):
            for col in range(len(location[0])):
                piece = Piece(row, col, location)
                color = piece.get_color()
                if color == "black" or color == "king_black":
                    self.pen.color("black", "black")
                elif color == "red" or color == "king_red":
                    self.pen.color("red", "red")
                else:
                    continue
                self.pen.setposition(self.cornor + col * self.square_size
                                     + self.square_size/2,
                                     self.cornor + row * self.square_size)
                self.draw_circle(self.square_size/2, color)

                is_king = piece.check_king()
                if is_king:
                    self.pen.color("white")
                    self.pen.setposition(self.cornor + col * self.square_size
                                         + self.square_size/2, self.cornor +
                                         row * self.square_size
                                         + self.square_size/3)
                    self.draw_circle(self.square_size/5, "white")

    def draw_shadow(self, x, y, color):
        '''
            Method -- draw_shadow
                Draw shadows to mark the position of the selected piece
                and the position where it can move.
            Parameters:
                self -- an instance of Turtle
                x -- the x Coordinate of the piece
                y -- the y Coordinate of the piece
                color -- the color of shadow
            Returns:
                Nothing. Draws shadows
        '''
        self.pen.color(color)
        self.pen.setposition(self.cornor + self.square_size * y,
                             self.cornor + self.square_size * x)
        self.draw_empty_square(self.square_size)

    def clear_shadow(self, color):
        '''
            Method -- clear_shadow
                Clear all shadows
            Parameters:
                self -- an instance of Turtle
                color -- the color of new shadow
            Returns:
                Nothing. clear
        '''
        self.pen.color(color)
        for col in range(self.num_squares):
            for row in range(self.num_squares):
                self.pen.setposition(self.cornor + self.square_size * col,
                                     self.cornor + self.square_size * row)
                self.draw_empty_square(self.square_size)
