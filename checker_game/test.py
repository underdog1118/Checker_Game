'''
Zhengpeng Qiu  CS5001-22Fall  Final Project
Description: pytest, some files which are directly
used turtle function cannot be tested
'''
import turtle
from game_state import GameState
from piece import Piece
from move import Move
from function import Function
from constants import SQUARE_SIZE, NUM_SQUARES
from perform import Perform

squares = [
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


# move class constructor
def test_move():
    move = Move("black", squares)
    assert (move.turn == "black")
    assert (move.squares == squares)


def test_position_converter():
    move = Move("red", squares)
    assert (move.position_converter(50, 50) == [(5, 5)])
    assert (move.position_converter(129, 123) == [(5, 5), (6, 6)])


def test_get_next_move():
    move = Move("red", squares)
    move.get_next_move(5, 2, 4, 1, 3, 0)
    assert (move.ava_normal_move == [(4, 1)])
    assert (move.ava_cap_move == [])


def test_non_king_move():
    move = Move("red", squares)
    move.non_king_move(5, 0)
    assert (move.ava_normal_move == [(4, 1)])
    assert (move.ava_cap_move == [])


def test_king_move():
    move = Move("red", [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "king_red", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "empty", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
            ])
    move.king_move(4, 4)
    assert move.ava_normal_move == [(5, 5), (5, 3), (3, 5), (3, 3)]
    assert move.ava_cap_move == []


# function class
def test_function():
    pen = turtle.Turtle()
    fuc = Function(pen, SQUARE_SIZE, "grey", NUM_SQUARES)
    assert (fuc.pen == pen)
    assert (fuc.square_size == SQUARE_SIZE)
    assert (fuc.square_colors == "grey")
    assert (fuc.num_squares == NUM_SQUARES)


# game_state class
def test_game_state():
    game_state = GameState()
    assert (game_state.squares == squares)
    assert (game_state.curr_player == "black")


def test_change_player():
    game_state = GameState()
    assert (game_state.change_player(True) == "black")
    assert (game_state.change_player(False) == "red")
    assert (game_state.change_player(False) == "black")


def test_normal_move():
    game_state = GameState()
    assert (game_state.normal_move(-1, -1) == squares)
    assert (game_state.normal_move((2, 1), (3, 0)) == [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "empty", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
            ])


def test_cap_move():
    game_state = GameState()
    game_state.squares = [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "empty", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "black", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "red", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "empty", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
            ]
    assert (game_state.cap_move((3, 2), (4, 3), (5, 4)) == [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "empty", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "black", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
            ])


def test_turn_to_king():
    game_state = GameState()
    game_state.squares = [
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "empty", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "red", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "empty", "empty", "red", "empty"],

            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "black", "red", "empty", "red", "empty"]
            ]
    assert (game_state.turn_to_king() ==
            [
        ["empty", "black", "empty", "black", "empty", "black", "empty",
            "black"],
        ["black", "empty", "black", "empty", "black", "empty", "black",
            "empty"],
        ["empty", "empty", "empty", "black", "empty", "black", "empty",
            "black"],
        ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
            "empty"],
        ["empty", "empty", "empty", "red", "empty", "empty", "empty",
            "empty"],
        ["red", "empty", "red", "empty", "empty", "empty", "red", "empty"],

        ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

        ["red", "empty", "red", "king_black", "red", "empty", "red", "empty"]
        ])


# piece class
def test_piece():
    piece = Piece(3, 3, squares)
    assert (piece.row == 3)
    assert (piece.col == 3)
    assert (piece.square == squares)


def test_get_color():
    piece_1 = Piece(3, 3, squares)
    piece_2 = Piece(7, 0, squares)
    piece_3 = Piece(0, 1, squares)
    assert (piece_1.get_color() == "empty")
    assert (piece_2.get_color() == "red")
    assert (piece_3.get_color() == "black")


def test_is_in_boundary():
    piece_1 = Piece(3, 3, squares)
    piece_2 = Piece(7, 0, squares)
    piece_3 = Piece(0, 9, squares)
    assert (piece_1.is_in_boundary() is True)
    assert (piece_2.is_in_boundary() is True)
    assert (piece_3.is_in_boundary() is False)


def test_get_opponent():
    piece_1 = Piece(3, 3, squares)
    piece_2 = Piece(7, 0, squares)
    piece_3 = Piece(0, 1, squares)
    assert (piece_1.get_opponent() is None)
    assert (piece_2.get_opponent() == "black")
    assert (piece_3.get_opponent() == "red")


def test_check_king():
    squares = [
            ["empty", "king_black", "empty", "black", "empty", "black",
             "empty", "black"],
            ["black", "empty", "black", "empty", "black", "empty", "black",
             "empty"],
            ["empty", "black", "empty", "black", "empty", "black", "empty",
             "black"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty",
             "empty"],
            ["red", "empty", "red", "empty", "red", "empty", "king_red",
             "empty"],
            ["empty", "red", "empty", "red", "empty", "red", "empty", "red"],

            ["red", "empty", "red", "empty", "red", "empty", "red", "empty"]
        ]
    piece_1 = Piece(3, 3, squares)
    piece_2 = Piece(7, 0, squares)
    piece_3 = Piece(0, 1, squares)
    assert (piece_1.check_king() is False)
    assert (piece_2.check_king() is False)
    assert (piece_3.check_king() is True)
