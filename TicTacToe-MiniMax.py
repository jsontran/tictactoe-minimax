from math import inf as infinity
from os import system
import platform

# Make a list of the board
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
firstGame = True


def DisplayBoard():
    # This function displays the board.
    # For loop for each row and collum,
    # and formats the players input accordingly.
    for i in range(0, 3):
        print('|', end="")
        for j in range(0, 3):
            print('{}|'.format(board[i][j]), end="")
        print()
    print()


def CheckResults():
    # Check for vertical win by cycling through the collums.
    for i in range(0, 3):
        if board[0][i] != '-' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check for horizontal win by cycling through the rows.
    for i in range(0, 3):
        if board[i] == ['X', 'X', 'X'] or board[i] == ['O', 'O', 'O']:
            return board[i][i]

    # Check for diagonal win by checking each direction.
    if ((board[0][0] != '-' and board[0][0] == board[1][1] and board[1][1] == board[2][2]) or
            (board[0][2] != '-' and board[0][2] == board[1][1] and board[1][1] == board[2][0])):
        return board[1][1]

    # No win returns false statement.
    return False


def PossibleMoves():
    # Create an enumerate list of unoccupied spots on the board.
    # Then return the list.
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == '-':
                cells.append([x, y])
    return cells


def SetMove(x, y, player):
    # If the position is unoccupied, return True
    if board[y][x] == '-':
        board[y][x] = player
        return True
    else:
        # If the position is occupied, print error message and return false.
        print('Please enter a valid position! (E:01)')
        return False


def MiniMax(board, depth, player, alpha, beta):

    # board: the current board in tic-tac-toe(node)
    # depth: index of the node in the game tree
    # player: may be a MAX player or MIN player

    # alpha: is negative infinity
    # beta: postive infintity
    #      --> both players start with worst possible scores
    if player == 'O':
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    # If the game has ended or there are no possible branches,
    # Give the score: +1 for maximizing to win
    #                 -1 for minimazing to win
    #                  0 for a tie
    if depth == 0 or CheckResults() != False:
        if CheckResults() == 'O':
            score = 1
        elif CheckResults() == 'X':
            score = -1
        else:
            score = 0
        return [-1, -1, score]

    # For every possible move, place the player(if maximizing or computer if minimizing)
    # recieve th score, revert the board, and determine if that is the best score.
    for cell in PossibleMoves():

        x, y = cell[0], cell[1]
        board[x][y] = player

        if player == 'O':
            score = MiniMax(board, depth - 1, 'X', alpha, beta)
        else:
            score = MiniMax(board, depth - 1, 'O', alpha, beta)

        board[x][y] = '-'
        score[0], score[1] = y, x

        # If maximizing, check if the current score is better than the previous
        # If score is better than or equal to beta, return as it is the best case
        # If score is better than alpha, make that the new alpha
        if player == 'O':
            if score[2] > best[2]:
                best = score  # max value
            if score[2] >= beta:
                return best
            if score[2] > alpha:
                alpha = score[2]
        else:
            # If minimizing, check if the current score is lower than the previous
            # If score is lower than or equal to alpha, return as it is the best case
            # If score is lower than beta, make that the new beta
            if score[2] < best[2]:
                best = score  # min value
            if score[2] <= alpha:
                return best
            if score[2] < beta:
                beta = score[2]

    return best


def PlayerMove():
    # Make a dictionary on the rows associated with the letters.
    dict = {'a': 0, 'b': 1, 'c': 2}
    # In a while loop, keep asking for a VALID position on the board.
    while True:
        position = list(
            input('Choose the Row (Letters) and Collum(Numbers) of the board (ex: A1): '))
        if len(position) == 2:
            try:
                # Translate the input into the position, intercept if input is invalid.
                py = dict[position[0].lower()]
                px = int(position[1]) - 1
                if SetMove(px, py, 'X'):
                    # Clear the board then break the while loop
                    Clear()
                    break
            except:
                print('Please enter a valid position! (E:02)')
        else:
            print('Please enter a valid position! (E:03)')


def CompMove():

    # Check if there is a winning result
    if CheckResults() != False:
        return
    # Determine the depth for the minimax function, with the list of possible moves.
    # Then get the best result of the minimax function, clean the console, and  set the move
    depth = len(PossibleMoves())
    move = MiniMax(board, depth, 'O', -infinity, infinity)
    x, y = move[0], move[1]

    Clear()
    SetMove(x, y, 'O')


def Clear():
    global firstGame
    firstGame = False
    # Check which OS the user is on, and then clear the console.
    OSname = platform.system().lower()
    if 'windows'.lower() in OSname:
        system('cls')
    else:
        system('clear')


def Play():
    # Clear concsole, display board, and ask player if they want to go first.
    Clear()

    starting = input('Do you want to go first? (Y/N):  ').upper()

    while True:
        if starting == 'Y':
            playerTurn = True
            break
        elif starting == 'N':
            playerTurn = False
            break
        else:
            starting = input('Do you want to go first? (Y/N):  ').upper()

    Clear()
    DisplayBoard()

    while True:
        # Loop checking results.
        CheckResults()

        # While there is unoccupied and there is no winning combination, play turns.
        while len(PossibleMoves()) > 0 and CheckResults() == False:
            if playerTurn:
                PlayerMove()
                DisplayBoard()
                playerTurn = False
            else:
                CompMove()
                DisplayBoard()
                playerTurn = True

        # If there is a winning result, determine which side won.
        if CheckResults() != False:
            if CheckResults() == 'X':
                print('Player Wins!')
            elif CheckResults() == 'O':
                print('Computer Wins!')
            break

        # If theres no winning results, but no more unoccupied position, its a tie!
        if len(PossibleMoves()) <= 0:
            print('Its a Tie!')
            break


# START THE GAME

while True:
    if firstGame:
        Play()
    elif firstGame == False:
        again = input('Do you want to play again? (Y/N):  ').upper()
        while True:
            if again == 'Y':
                board = [['-', '-', '-'],
                         ['-', '-', '-'],
                         ['-', '-', '-']]
                Play()
                break
            elif again == 'N':
                print('The End')
                break
            else:
                again = input('Do you want to play again? (Y/N):  ').upper()
