import random


board = [' ' for x in range(10)]

def insertBoard(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def isWinner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or 
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
    (bo[0] == le and bo[3] == le and bo[6] == le) or # down the left side
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the middle
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the right side
    (bo[2] == le and bo[4] == le and bo[6] == le) or # diagonal
    (bo[0] == le and bo[4] == le and bo[8] == le)) # diagonal
 
def playerMove():
    run = True
    while run:
        move = input('Please select a postition to place an \'X\' (1-9) ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move - 1):
                    run = False
                    insertBoard('X', move - 1)
                else:
                    print('Sorry, this space is occupied!')
            else: 
                print('Please type a number within the range!')
        except:
            print('Please type a number')

def selectRandom(li):
    ln = len(li) 
    r = random.randrange(0, ln)
    return li[r]
    
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = -1
    
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(board, let):
                move = i
                return move
            
    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
        
        if len(cornersOpen) > 0:
            move = selectRandom(cornersOpen)
            return move
        
        if 4 in possibleMoves:
            move = 4
            return move
        
        edgesOpen = []
        for i in possibleMoves:
            if i in [0,2,6,8]:
                edgesOpen.append(i)
    
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
        else:    
            move = selectRandom(possibleMoves)
    
        
        return move
      
    
    
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def printBoard():
    print('  |   |')
    print(' ' + board[0] + '| ' + board[1] + ' | ' + board[2])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' ' + board[3] + '| ' + board[4] + ' | ' + board[5])
    print('  |   |')
    print('-----------')
    print('  |   |')
    print(' ' + board[6] + '| ' + board[7] + ' | ' + board[8])
    print('  |   |')

def main():
    print('Welcome to Tic Tac Toe')
    printBoard()
    
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('Sorry, O\'s won this time!')
            break
       
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == -1:
                print('Tie Game')
            else:  
                insertBoard('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard()
        else:
            print('Sorry, X\'s won this time! Good Job!')
            break
        
    
    if isBoardFull(board):
        print('Tie Game!')
    
main()    
    