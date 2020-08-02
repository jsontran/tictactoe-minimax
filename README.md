# tictactoe-minimax
A Python implementation of Minimax AI Algorithm with Alpha-Beta pruning in the Tic-Tac-Toe game.

## Tic Tac Toe
It is a game where the two players take turns placing their symbols (either X's or O's) to achieve three in a row. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. In this version, the player will be against the computer (which uses the Minimax Algorithm with Alpha-Beta Pruning). 

#### Game Walkthrough
Initially, the game will ask if the player would like to go first, if they do not, the computer (O's) will make the first move.   
The game will ask the player for the row, and collum of the placement they desire.  
The rows are labeled with letters, and the collums are labeled with numbers (ex: A1 for top left).  
This will continue until the game comes to a conclusion. Afterwards it will ask to play once again.

## Minimax Algorithm 
The Minimax function will be maximizing the computers turns while trying to minimize the players turns.   
The comments in the code includes very brief definitions and explaination of the code.

Initially it sets the maximizing/minimizing scores to the worst case scenario (-infinity/+infinity). It then checks the current state of the game if there is a conclusion in the game giving the scores:  

+1 for maximizing to win.  
-1 for minimazing to win.  
0 for a tie.  

![](https://github.com/jtefano/tictactoe-minimax/blob/master/preview/1.JPG)

Afterwards, the function will go through every possible move with both the players and the computers symbols. After placing the symbol in an unoccupied space, it will recieve a score then revert the board back to its original state (before the function). It then recieves a new score, this is looped for all possible moves and combination availble. Once it finishes, it returns the best possible move for the computer.

![](https://github.com/jtefano/tictactoe-minimax/blob/master/preview/2.JPG)

## Minimax Algorithm with Alpha-Beta Pruning
Alpha–Beta pruning is a  seeks to reduce the number of nodes created by the minimax algorithm in its search tree (for all possible moves that can be made). It stops looking within the the branches/nodes when it came to the conclusion that this move is worst than a previously examined move. This shortens the time the minimax function takes by ignoring deemed unnessary nodes.

![](https://github.com/jtefano/tictactoe-minimax/blob/master/preview/3.JPG)

## Sources:
https://en.wikipedia.org/wiki/Minimax  
https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
https://becominghuman.ai/practical-artificial-intelligence-for-game-development-5b0ebf35993b
