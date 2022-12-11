# Checker_Game
Final project in CS5001 -- Intensive Foundation of Computer Science at Northeastern University
Project Expectations: Functionality

Implementation of Checkers does not have to look and function exactly like mine. Here are the expectations:

● You must display a board with an 8 x 8 checkerboard pattern made up of light and dark squares. You can change the overall dimensions of the board and the specific colors used, as long as you have the right number of squares and the top left square is your dark color.

● Each player starts with 12 pieces, arranged as shown in the first image in this document. Black and red are the traditional colors. You may change the colors but, if you do, be sure to document which color makes the first move.

● Moves must follow the rules above. If a capturing move is available, the player MUST make that move. If multiple capturing moves are available, it doesn’t matter which one is chosen, as long as a capture is made. If, after a player has captured an enemy piece, another capture is possible for the same piece, that capture must also be made.

● When a capture is made, the captured piece must be removed from the board.

● When a piece reaches the opposite side, it should be made into a King piece. King pieces should be visually distinguishable from “normal” pieces. You don’t have to use the same styling that I did. King pieces should be able to move as described above.

● One player is a (human) user, the other player is the computer. The human user should make the first move. If you’re sticking to the traditional colors, black will be human. When it’s the computer’s turn, your program will need to identify all legal moves and pick one to make. If a capturing move is available, it must be made. Beyond that, it’s up to you to decide how “smart” the computer should be when it picks a move.

● The user should make moves by clicking on the square containing the piece they would like to move, then clicking on the square the piece should be moved to. Only allow a move to be made if it is valid according to the rules above. If the user CS5001 Seattle Fall 2021

attempts an invalid move (e.g. clicking on an empty square or an enemy’s piece etc.), provide some feedback. Printing a message to the terminal counts as feedback.

● Update the UI appropriately after each move.

● When the game is over, declare the winner and stop the game play. In my implementation, the winner is printed in the UI but this is not required—printing to the terminal will meet this requirement.
