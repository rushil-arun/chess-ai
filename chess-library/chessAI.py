import pygame
import copy
import random
from chessPieceTables import pawns, knights, bishops, kingMiddle
from math import sqrt

chessBook = open("chess-library/book.txt", "r")

boardLetterDict = {
    "a": 0,
    'b': 1,
    "c": 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
}

boardNumberDict = {
    0: 8,
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1,
}

pieceConversions = {
    'K': "King",
    'B': "Bishop",
    'Q': "Queen",
    'R': "Rook",
    'N': "Knight",
}

gameBoard = [
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
]

boards = []

size = 640
tileSize = size // 8
black = (0, 0, 0)
white = (255, 255, 255)
peach = (255,218,185)
lavender = (255,240,245)
lightGreen = (204, 255, 153)
turqoise = (153, 255, 204)
red = (255, 0, 0)

currentPiece = None
oldPos = None

window = pygame.display.set_mode((size, size))

black_pawn = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_pawn.png")
black_king = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_king.png")
black_queen = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_queen.png")
black_rook = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_rook.png")
black_bishop = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_bishop.png")
black_knight = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/black_knight.png")
white_pawn = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_pawn.png")
white_king = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_king.png")
white_queen = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_queen.png")
white_rook = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_rook.png")
white_bishop = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_bishop.png")
white_knight = pygame.image.load("C:/Users/Rushil/Documents/GameCode/chess-library/Wikimedia Chess Pieces/white_knight.png")
piecePointMultiplier = 6
positions = 0
piecePoints = {
    'Pawn': 10 * piecePointMultiplier,
    'Knight': 30 * piecePointMultiplier,
    'Bishop': 30 * piecePointMultiplier,
    'Rook': 50 * piecePointMultiplier,
    'Queen': 90 * piecePointMultiplier,
    'King': 500 * piecePointMultiplier,
}

pieceTables = {
    'Pawn': pawns,
    'Knight': knights,
    'Bishop': bishops,
    'King': kingMiddle,
}

reverseList = {
    0: 7,
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
    7: 0,

}

def pythagorean(x, y):
    return sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2)

class Board:
    def __init__(self):
        self.board = gameBoard
        self.size = 8
        

    def setUpBoard(self):

        self.board[7][4] = Piece(white_king, 'King', white, 7, 4)
        self.board[5][4] = Piece(black_king, 'King', white, 5, 4)
        self.board[6][0] = Piece(black_queen, 'Queen', black, 6, 0)
        

        # # pawns
        # for y in range(self.size):
        #      black_pawn_clss = Piece(black_pawn, 'Pawn', black, 1, y)
        #      white_pawn_clss = Piece(white_pawn, 'Pawn', white, 6, y)
        #      self.board[1][y] = black_pawn_clss
        #      self.board[6][y] = white_pawn_clss

        # # kings
        # black_king_clss = Piece(black_king, 'King', black, 0, 4)
        # white_king_clss = Piece(white_king, 'King', white, 7, 4)
        # self.board[0][4] = black_king_clss
        # self.board[7][4] = white_king_clss

        # # queens

        # self.board[0][3] = Piece(black_queen, 'Queen', black, 0, 3)
        
        # self.board[7][3] = Piece(white_queen, 'Queen', white, 7, 3)

        # # rooks

        # left_black_rook_clss = Piece(black_rook, 'Rook', black, 0, 0)
        # right_black_rook_clss = Piece(black_rook, 'Rook', black, 0, 7)
        # left_white_rook_clss = Piece(white_rook, 'Rook', white, 7, 0)
        # right_white_rook_clss = Piece(white_rook, 'Rook', white, 7, 7)
        # self.board[0][0] = left_black_rook_clss
        # self.board[0][7] = right_black_rook_clss
        # self.board[7][0] = left_white_rook_clss
        # self.board[7][7] = right_white_rook_clss

        # # bishops
        # left_black_bishop_clss = Piece(black_bishop, 'Bishop', black, 0, 2)
        # right_black_bishop_clss = Piece(black_bishop, 'Bishop', black, 0, 5)
        # left_white_bishop_clss = Piece(white_bishop, 'Bishop', white, 7, 2)
        # right_white_bishop_clss = Piece(white_bishop, 'Bishop', white, 7, 5)
        # self.board[0][2] = left_black_bishop_clss
        # self.board[0][5] = right_black_bishop_clss
        # self.board[7][2] = left_white_bishop_clss
        # self.board[7][5] = right_white_bishop_clss

        # #knights
        # left_black_knight_clss = Piece(black_knight, 'Knight', black, 0, 1)
        # right_black_knight_clss = Piece(black_knight, 'Knight', black, 0, 6)
        # left_white_knight_clss = Piece(white_knight, 'Knight', white, 7, 1)
        # right_white_knight_clss = Piece(white_knight, 'Knight', white, 7, 6)
        # self.board[0][1] = left_black_knight_clss
        # self.board[0][6] = right_black_knight_clss
        # self.board[7][1] = left_white_knight_clss
        # self.board[7][6] = right_white_knight_clss

        
        

    def drawBoard(self):
        for x in range(self.size):
            for y in range(self.size):
                if (x + y) % 2 == 0:
                    pygame.draw.rect(window, peach, (x * tileSize, y * tileSize, tileSize, tileSize))
                else:
                    pygame.draw.rect(window, lavender, (x * tileSize, y * tileSize, tileSize, tileSize))



class Piece:
    
    def __init__(self, img, piece, color, row, cell):

        self.border = 5
        self.img = img
        self.img = pygame.transform.scale(self.img, (tileSize - (self.border), tileSize - self.border))
        self.width = self.img.get_size()[0]
        self.height = self.img.get_size()[1]
        self.piece = piece
        self.color = color
        self.row = row
        self.isLifted = False
        self.cell = cell
        #self.x = self.cell * tileSize
        #self.y = self.row * tileSize
        self.hasMoved = False

    def draw(self):
        self.img = pygame.transform.scale(self.img, (tileSize - (self.border), tileSize - (self.border)))
        window.blit(self.img, (((self.cell * tileSize) + (self.border // 2), (self.row * tileSize) + (self.border // 2))))
        #window.blit(self.img, (self.x + (self.border // 2), self.y + (self.border // 2)))

        
def legalMoves(board, piece, color, gameTurn, row, cell, hasMoved, shouldCheckCheck):
        
    legalMoves = []

    
    # pawn
    if piece == 'Pawn':
        if color == white:
            # if row != 0 and board[row - 1][cell] != '':
            #     if cell == 7:
            #         if board[row - 1][cell - 1] == '':
            #             return [(row, cell)]
            #     elif cell == 0:
            #         if board[row - 1][cell + 1] == '':
            #             return [(row, cell)]
            #     else:
            #         if board[row - 1][cell - 1] == '' and board[row - 1][cell + 1] == '':
            #             return [(row, cell)]
            
            if cell != 0 and row != 0 and board[row - 1][cell - 1] != '' and board[row - 1][cell - 1].color != white:
                legalMoves.append((row - 1, cell - 1))
            
            if cell != 7 and row != 0 and board[row - 1][cell + 1] != '' and board[row - 1][cell + 1].color != white:
                legalMoves.append((row - 1, cell + 1))

            if not hasMoved:
                if board[row - 2][cell] != '' and board[row - 1][cell] == '':
                    legalMoves.append((row - 1, cell))
                elif board[row - 2][cell] == '' and board[row - 1][cell] == '':
                    legalMoves.append((row - 1, cell))
                    legalMoves.append((row - 2, cell))
            else:
                if board[row - 1][cell] == '':
                    legalMoves.append((row - 1, cell))
                
        else:
            # if row != 7 and board[row + 1][cell] != '':
            #     if cell == 7:
            #         if board[row + 1][cell - 1] == '':
            #             return [(row, cell)]
            #     elif cell == 0:
            #         if board[row + 1][cell + 1] == '':
            #             return [(row, cell)]
            #     else:
            #         if board[row + 1][cell - 1] == '' and board[row + 1][cell + 1] == '':
            #             return [(row, cell)]
            
            if cell != 0 and row != 7 and board[row + 1][cell - 1] != '' and board[row + 1][cell - 1].color != black:
                legalMoves.append((row + 1, cell - 1))
            
            if cell != 7 and row != 7 and board[row + 1][cell + 1] != '' and board[row + 1][cell + 1].color != black:
                legalMoves.append((row + 1, cell + 1))

            if not hasMoved:
                if board[row + 2][cell] != '' and board[row + 1][cell] == '':
                    legalMoves.append((row + 1, cell))
                elif board[row + 2][cell] == '' and board[row + 1][cell] == '':
                    legalMoves.append((row + 1, cell))
                    legalMoves.append((row + 2, cell))

            else:
                if board[row + 1][cell] == '':
                    legalMoves.append((row + 1, cell))

        if shouldCheckCheck:
            #print(legalMoves)
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)

        #legalMoves.append((row, cell))

        

    

        return legalMoves

    elif piece == 'Bishop':
        # color doesn't matter
        # check i + current row to see if bishop hits end (because it won't be in starting position)
        
        for i in range(1, 8):
            if row == 0 or cell == 0 or row - i < 0 or cell - i < 0 or board[row - i][cell - i] != '':
                if row != 0 and cell != 0 and row - i >= 0 and cell - i >= 0 and board[row - i][cell - i].color != color:
                    legalMoves.append((row - i, cell - i))
                break
            legalMoves.append((row - i, cell - i))

        for i in range(1, 8):
            if row == 7 or cell == 7 or row + i > 7 or cell + i > 7 or board[row + i][cell + i] != '':
                if row != 7 and cell != 7 and row + i <= 7 and cell + i <= 7 and board[row + i][cell + i].color != color:
                    legalMoves.append((row + i, cell + i))
                break
            legalMoves.append((row + i, cell + i))
        
        for i in range(1, 8):
            if row == 0 or cell == 7 or row - i < 0 or cell + i > 7 or board[row - i][cell + i] != '':
                if row != 0 and cell != 7 and row - i >= 0 and cell + i <= 7 and board[row - i][cell + i].color != color:
                    legalMoves.append((row - i, cell + i))
                break
            legalMoves.append((row - i, cell + i))

        for i in range(1, 8):
            if row == 7 or cell == 0 or row + i > 7 or cell - i < 0 or board[row + i][cell - i] != '':
                if row != 7 and cell != 0 and row + i <= 7 and cell - i >= 0 and board[row + i][cell - i].color != color:
                    legalMoves.append((row + i, cell - i))
                break
            legalMoves.append((row + i, cell - i))

        

        if shouldCheckCheck:
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)

        #legalMoves.append((row, cell))

        return legalMoves
      

    elif piece == 'Rook':

        for i in range(1, 8):
            if row == 0 or row - i < 0 or board[row - i][cell] != '':
                if row != 0 and row - i >= 0 and board[row - i][cell].color != color:
                    legalMoves.append((row - i, cell))
                break
            legalMoves.append((row - i, cell))

        for i in range(1, 8):
            if row == 7 or row + i > 7 or board[row + i][cell] != '':
                if row != 7 and row + i <= 7 and board[row + i][cell].color != color:
                    legalMoves.append((row + i, cell))
                break
            legalMoves.append((row + i, cell))
        
        for i in range(1, 8):
            if cell == 0 or cell - i < 0 or board[row][cell - i] != '':
                if cell != 0 and cell - i >= 0 and board[row][cell - i].color != color:
                    legalMoves.append((row, cell - i))
                break
            legalMoves.append((row, cell - i))

        for i in range(1, 8):
            if cell == 7 or cell + i > 7 or board[row][cell + i] != '':
                if cell != 7 and cell + i <= 7 and board[row][cell + i].color != color:
                    legalMoves.append((row, cell + i))
                break
            legalMoves.append((row, cell + i))

        if shouldCheckCheck:
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)

        #legalMoves.append((row, cell))

        return legalMoves

    elif piece == 'Queen':
        for i in range(1, 8):
            if row == 0 or cell == 0 or row - i < 0 or cell - i < 0 or board[row - i][cell - i] != '':
                if row != 0 and cell != 0 and row - i >= 0 and cell - i >= 0 and board[row - i][cell - i].color != color:
                    legalMoves.append((row - i, cell - i))
                break
            legalMoves.append((row - i, cell - i))

        for i in range(1, 8):
            if row == 7 or cell == 7 or row + i > 7 or cell + i > 7 or board[row + i][cell + i] != '':
                if row != 7 and cell != 7 and row + i <= 7 and cell + i <= 7 and board[row + i][cell + i].color != color:
                    legalMoves.append((row + i, cell + i))
                break
            legalMoves.append((row + i, cell + i))
        
        for i in range(1, 8):
            if row == 0 or cell == 7 or row - i < 0 or cell + i > 7 or board[row - i][cell + i] != '':
                if row != 0 and cell != 7 and row - i >= 0 and cell + i <= 7 and board[row - i][cell + i].color != color:
                    legalMoves.append((row - i, cell + i))
                break
            legalMoves.append((row - i, cell + i))

        for i in range(1, 8):
            if row == 7 or cell == 0 or row + i > 7 or cell - i < 0 or board[row + i][cell - i] != '':
                if row != 7 and cell != 0 and row + i <= 7 and cell - i >= 0 and board[row + i][cell - i].color != color:
                    legalMoves.append((row + i, cell - i))
                break
            legalMoves.append((row + i, cell - i))

        for i in range(1, 8):
            if row == 0 or row - i < 0 or board[row - i][cell] != '':
                if row != 0 and row - i >= 0 and board[row - i][cell].color != color:
                    legalMoves.append((row - i, cell))
                break
            legalMoves.append((row - i, cell))

        for i in range(1, 8):
            if row == 7 or row + i > 7 or board[row + i][cell] != '':
                if row != 7 and row + i <= 7 and board[row + i][cell].color != color:
                    legalMoves.append((row + i, cell))
                break
            legalMoves.append((row + i, cell))
        
        for i in range(1, 8):
            if cell == 0 or cell - i < 0 or board[row][cell - i] != '':
                if cell != 0 and cell - i >= 0 and board[row][cell - i].color != color:
                    legalMoves.append((row, cell - i))
                break
            legalMoves.append((row, cell - i))

        for i in range(1, 8):
            if cell == 7 or cell + i > 7 or board[row][cell + i] != '':
                if cell != 7 and cell + i <= 7 and board[row][cell + i].color != color:
                    legalMoves.append((row, cell + i))
                break
            legalMoves.append((row, cell + i))

        if shouldCheckCheck:
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)


        #legalMoves.append((row, cell))

        return legalMoves

    elif piece == 'King':

        for i in range(-1, 2):
            if row > 0 and cell + i >= 0 and cell + i <= 7 and (board[row - 1][cell + i] == '' or board[row - 1][cell + i].color != color):
                legalMoves.append((row - 1, cell + i))

            if row < 7 and cell + i >= 0 and cell + i <= 7 and (board[row + 1][cell + i] == '' or board[row + 1][cell + i].color != color):
                legalMoves.append((row + 1, cell + i))
        
        if cell > 0 and (board[row][cell - 1] == '' or board[row][cell - 1].color != color):
            legalMoves.append((row, cell - 1))
        
        if cell < 7 and (board[row][cell + 1] == '' or board[row][cell + 1].color != color):
            legalMoves.append((row, cell + 1))

        if shouldCheckCheck:
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)
        #print(legalMoves)
        #legalMoves.append((row, cell))


        return legalMoves

    elif piece == 'Knight':
        
         
        if row > 1 and cell > 0 and (board[row - 2][cell - 1] == '' or board[row - 2][cell - 1].color != color):
            legalMoves.append((row - 2, cell - 1))


        if row > 1 and cell < 7 and (board[row - 2][cell + 1] == '' or board[row - 2][cell + 1].color != color):
            legalMoves.append((row - 2, cell + 1))

        if row < 6 and cell > 0 and (board[row + 2][cell - 1] == '' or board[row + 2][cell - 1].color != color):
            legalMoves.append((row + 2, cell - 1))
        
        if row < 6 and cell < 7 and (board[row + 2][cell + 1] == '' or board[row + 2][cell + 1].color != color):
            legalMoves.append((row + 2, cell + 1))

        if row > 0 and cell < 6 and (board[row - 1][cell + 2] == '' or board[row - 1][cell + 2].color != color):
            legalMoves.append((row - 1, cell + 2))

        if row < 7 and cell < 6 and (board[row + 1][cell + 2] == '' or board[row + 1][cell + 2].color != color):
            legalMoves.append((row + 1, cell + 2))

        if row > 0 and cell > 1 and (board[row - 1][cell - 2] == '' or board[row - 1][cell - 2].color != color):
            legalMoves.append((row - 1, cell - 2))

        if row < 7 and cell > 1 and (board[row + 1][cell - 2] == '' or board[row + 1][cell - 2].color != color):
            legalMoves.append((row + 1, cell - 2))
        
        if shouldCheckCheck:
            for i in legalMoves[:]:
                if moveOutOfCheck(board, i[0], i[1], row, cell, board[i[0]][i[1]], board[row][cell], color, gameTurn):
                    legalMoves.remove(i)
        #print(legalMoves)
        #legalMoves.append((row, cell))

        

        return legalMoves

def promote(board):
    for x in range(8):
        if board[0][x] != '':
            if board[0][x].piece == 'Pawn' and board[0][x].color == white and not isKingInCheck(white, board, 0):
                board[0][x].piece = 'Queen'
                board[0][x].img = white_queen

                break
        if board[7][x] != '':

            if board[7][x].piece == 'Pawn' and board[0][x].color == black and not isKingInCheck(black, board, 0):
                board[7][x].piece = 'Queen'
                board[0][x].img = black_queen
                break

    
def castleRightWhite(board, lst, gameTurn):
    if board[7][5] == '' and board[7][6] == '' and board[7][4] != '' and board[7][4].piece == 'King' and board[7][4].color == white and board[7][4].hasMoved == False:
        if board[7][7] != '' and board[7][7].piece == 'Rook' and board[7][7].color == white and board[7][7].hasMoved == False:
            if not moveOutOfCheck(board, 7, 5, 7, 4, '', board[7][4], white, gameTurn) and not moveOutOfCheck(board, 7, 6, 7, 4, '', board[7][4], white, gameTurn):
                lst.append((7, 6))
                return lst, [7, 6]

    return lst, [-1, -1]

def castleLeftWhite(board, lst, gameTurn):
    if board[7][1] == '' and board[7][2] == '' and board[7][3] == '' and board[7][4] != '' and board[7][4].piece == 'King' and board[7][4].color == white and board[7][4].hasMoved == False:
        if board[7][0] != '' and board[7][0].piece == 'Rook' and board[7][0].color == white and board[7][0].hasMoved == False:
            if not moveOutOfCheck(board, 7, 2, 7, 4, '', board[7][4], white, gameTurn) and not moveOutOfCheck(board, 7, 3, 7, 4, '', board[7][4], white, gameTurn):
                lst.append((7, 2))
                return lst, [7, 2]

    return lst, [-1, -1]

def castleRightBlack(board, lst, gameTurn):
    if board[0][5] == '' and board[0][6] == '' and board[0][4] != '' and board[0][4].piece == 'King' and board[0][4].color == black and board[0][4].hasMoved == False:
        if board[0][7] != '' and board[0][7].piece == 'Rook' and board[0][7].color == black and board[0][7].hasMoved == False:
            if not moveOutOfCheck(board, 0, 5, 0, 4, '', board[0][4], black, gameTurn) and not moveOutOfCheck(board, 0, 6, 0, 4, '', board[0][4], black, gameTurn):
                lst.append((0, 6))
                return lst, [0, 6]

    return lst, [-1, -1]

def castleLeftBlack(board, lst, gameTurn):
    if board[0][1] == '' and board[0][2] == '' and board[0][3] == '' and board[0][4] != '' and board[0][4].piece == 'King' and board[0][4].color == black and board[0][4].hasMoved == False:
        if board[0][0] != '' and board[0][0].piece == 'Rook' and board[0][0].color == black and board[0][0].hasMoved == False:
            if not moveOutOfCheck(board, 0, 2, 0, 4, '', board[0][4], black, gameTurn) and not moveOutOfCheck(board, 0, 3, 0, 4, '', board[0][4], black, gameTurn):
                lst.append((0, 2))
                return lst, [0, 2]

    return lst, [-1, -1]




def castle(row, cell, castleSquareWhiteRight, castleSquareWhiteLeft, castleSquareBlackRight, castleSquareBlackLeft, board):
    if (row) == castleSquareWhiteRight[0] and cell == castleSquareWhiteRight[1]:
        board[7][5] = board[7][7]
        board[7][5].row = 7
        board[7][5].cell = 5
        board[7][7] = ''
        board[7][5].hasMoved = True
    elif (row == castleSquareWhiteLeft[0] and cell == castleSquareWhiteLeft[1]):
        board[7][3] = board[7][0]
        board[7][3].row = 7
        board[7][3].cell = 3
        board[7][0] = ''
        board[7][3].hasMoved = True
    elif (row == castleSquareBlackRight[0] and cell == castleSquareBlackRight[1]):
        board[0][5] = board[0][7]
        board[0][5].row = 0
        board[0][5].cell = 5
        board[0][7] = ''
        board[0][5].hasMoved = True
    elif row == castleSquareBlackLeft[0] and cell == castleSquareBlackLeft[1]:
        board[0][3] = board[0][0]
        board[0][3].row = 0
        board[0][3].cell = 3
        board[0][0] = ''
        board[0][3].hasMoved = True

    return board

def isKingInCheck(kingCol, board, gameTurn):
    #print("Hello")
    col = white if kingCol == black else black
    totalMoves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != '' and board[x][y].color == col:                   
                pieceMoves = legalMoves(
                    board,
                    board[x][y].piece, 
                    board[x][y].color,
                    gameTurn,
                    board[x][y].row,
                    board[x][y].cell,
                    board[x][y].hasMoved,
                    False
                )
                for i in pieceMoves:
                    totalMoves.append(i)

    for i in totalMoves:
        if board[i[0]][i[1]] != '' and board[i[0]][i[1]].piece == 'King' and board[i[0]][i[1]].color == kingCol:
            return True

    return False

def moveOutOfCheck(currentBoard, row1, cell1, row2, cell2, oldPieceClass, pieceClass, color, gameTurn):
    # this is messing with the board.
    currentBoard[row1][cell1] = pieceClass
    currentBoard[row2][cell2] = ''

    # for i in range(8):
    #     print(currentBoard[i])

    # print("________________________________________")

    if isKingInCheck(color, currentBoard, gameTurn):
        #print("CHECK")
        currentBoard[row1][cell1] = oldPieceClass
        currentBoard[row2][cell2] = pieceClass
        return True
    currentBoard[row1][cell1] = oldPieceClass
    currentBoard[row2][cell2] = pieceClass
    return False

def checkMate(color, board, gameTurn):
    moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != '' and board[x][y].color == color:
                pieceMoves = legalMoves(board, board[x][y].piece, color, gameTurn, x, y, board[x][y].hasMoved, True)
                for i in pieceMoves:
                    moves.append(i)
            

    if isKingInCheck(color, board, gameTurn) and len(moves) == 0:
        return True
    return False
                    

def checkPawns(board, color):
    # isolated pawns
    isolatedPawns = 0
    for x in range(8):
        for y in range(1, 7):
            if board[x][y] != '' and board[x][y].piece == 'Pawn':
                pass
    
    doubledPawns = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] != '' and board[x][y].piece == 'Pawn' and board[x][y].color == white:
                pass

def evaluateBoard(board, color, moves):
    whiteScore = 0
    blackScore = 0
    whiteQueen = None
    blackQueen = None
    whiteKing = None
    blackKing = None
    for x in range(8):
        for y in range(8):
            if board[x][y] != '' and board[x][y].piece == 'King' and board[x][y].color == black:
                blackKing = [x, y]
            if board[x][y] != '' and board[x][y].piece == 'King' and board[x][y].color == white:
                whiteKing = [x, y]
            if board[x][y] != '' and board[x][y].piece == 'Queen' and board[x][y].color == black:
                blackQueen = [x, y]
            if board[x][y] != '' and board[x][y].piece == 'Queen' and board[x][y].color == white:
                whiteQueen = [x, y]

            if board[x][y] != '' and board[x][y].color == white and board[x][y].piece != 'Queen' and board[x][y].piece != 'Rook':
                whiteScore += piecePoints[board[x][y].piece]
                whiteScore += pieceTables[board[x][y].piece][x][y] * 1.1
            elif board[x][y] != '' and board[x][y].color == black and board[x][y].piece != 'Queen' and board[x][y].piece != 'Rook':
                blackScore += piecePoints[board[x][y].piece]
                blackScore += pieceTables[board[x][y].piece][reverseList[x]][reverseList[y]] * 1.1
            if board[x][y] != '':
                if board[x][y].piece == 'Queen' or board[x][y].piece == 'Rook':
                    if board[x][y].color == black:
                        blackScore += piecePoints[board[x][y].piece]
                    else:
                        whiteScore += piecePoints[board[x][y].piece]

    #whiteMoves = generateAllMoves(white, board)
    #blackMoves = generateAllMoves(black, board)

    if blackKing != None and whiteQueen != None:
        blackScore -= pythagorean(blackKing, whiteQueen) * 5
    if whiteKing != None and blackQueen != None:
        whiteScore -= pythagorean(whiteKing, blackQueen) * 5
    # kingDistance = pythagorean(blackKing, whiteKing) * 30
    # blackScore += kingDistance
    # whiteScore -= kingDistance

    if color == white:
        whiteScore += len(moves) * 3
    else:
        blackScore += len(moves) * 3

    #whiteScore += len(whiteMoves) * 2
    #blackScore += len(blackMoves) * 2

    return blackScore - whiteScore

def generateAllMoves(color, board):
    totalMoves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != '' and board[x][y].color == color:                   
                pieceMoves = legalMoves(
                    board,
                    board[x][y].piece, 
                    board[x][y].color,
                    0,
                    board[x][y].row,
                    board[x][y].cell,
                    board[x][y].hasMoved,
                    True
                )
                #print(pieceMoves, board.board[x][y].piece, board.board[x][y].color)
                #pygame.time.delay(1000)
                for i in pieceMoves:
                    totalMoves.append([x, y, i[0], i[1], board[i[0]][i[1]]])
        

    return totalMoves

def removeCaptures(board, turn, alpha, beta):
    moves = generateAllMoves(turn, board)
    bestScore = -(float('inf'))
    #bestMove = None
    for i in moves[:]:
        if board[i[2]][i[3]] == '':
            moves.remove(i)

    for i in moves:
        board[i[2]][i[3]] = board[i[0]][i[1]]
        board[i[0]][i[1]] = ''
        turn = white if turn == black else black
        evaluation = removeCaptures(board, turn, -alpha, -beta)
        board[i[0]][i[1]] = board[i[2]][i[3]]
        board[i[2]][i[3]] = i[4]

        if evaluation > bestScore:
            bestScore = evaluation
            #bestMove = i

    return bestScore



def algorithm(depth, board, alpha, beta, maxPlayer, turn, passedMoves):
    global positions, boards
    # Make it keep evaluating until there are no checks
    if checkMate(white, board, 0):
        print("white has been mated")
        positions += 1
        return float('inf'), depth
    elif checkMate(black, board, 0):
        print("black has been mated")
        positions += 1
        return -float('inf'), depth
    elif depth == 0:
        positions += 1
        #return removeCaptures(board, turn, alpha, beta)
        return evaluateBoard(board, turn, passedMoves), depth

    if maxPlayer:
        bestScore = -(float('inf'))
        bestDepth = (float('inf'))
        totalMoves = generateAllMoves(turn, board)
        # totalMoves, posRight = castleRightBlack(board, totalMoves, 0)
        # totalMoves, posLeft = castleLeftBlack(board, totalMoves, 0)
        for i in totalMoves:
            # if i == posRight: # CASTLING
            #     board[posRight[0]][posRight[1]] = board[0][4]
            #     board[0][4] = ''

            board[i[2]][i[3]] = board[i[0]][i[1]]
            board[i[0]][i[1]] = ''
            algScore = algorithm(depth - 1, board, alpha, beta, False, white, totalMoves)
            board[i[0]][i[1]] = board[i[2]][i[3]]
            board[i[2]][i[3]] = i[4]
            if algScore[0] > bestScore:
                bestScore = algScore[0]
                bestMove = i
                bestDepth = algScore[1]
            elif algScore[0] == bestScore:
                if algScore[1] < bestDepth:
                    bestScore = algScore[0]
                    bestMove = i
                    bestDepth = algScore[1]
            alpha = max(alpha, bestScore)
            if beta <= alpha:
                break
            

        return bestScore, bestDepth
    
    else:
        bestScore = float('inf')
        bestDepth = float('inf')
        totalMoves = generateAllMoves(turn, board)
        # totalMoves, pos = castleRightWhite(board, totalMoves, 0)
        # totalMoves, pos = castleLeftWhite(board, totalMoves, 0)
        for i in totalMoves:
            board[i[2]][i[3]] = board[i[0]][i[1]]
            board[i[0]][i[1]] = ''
            boards.append(board)
            algScore = algorithm(depth - 1, board, alpha, beta, True, black, totalMoves)
            board[i[0]][i[1]] = board[i[2]][i[3]]
            board[i[2]][i[3]] = i[4]
            if algScore[0] < bestScore:
                bestScore = algScore[0]
                bestMove = i
                bestDepth = algScore[1]
            elif algScore[0] == bestScore:
                if algScore[1] < bestDepth:
                    bestScore = algScore[0]
                    bestMove = i
                    bestDepth = algScore[1]
            beta = min(beta, bestScore)
            if beta <= alpha:
                break
            

        return bestScore, bestDepth
    

def pickMove(board, turn, depth):
    global currentPiece, oldPos
    movesList = []
    
    bestScore = -(float('inf'))
    bestDepth = float('inf')
    bestMove = None
    #pygame.time.delay(500)
    # for i in range(8):
    #     for x in range(8):
    #         if board.board[i][x] != '':
    #             print(board.board[i][x].piece, end=' ')
    #         else:
    #             print("Empty", end = ' ')

    # print("____________________________________-")
    totalMoves = generateAllMoves(turn, board)
    # totalMoves, pos = castleRightBlack(board, totalMoves, 0)
    # totalMoves, pos = castleLeftBlack(board, totalMoves, 0)
    for i in totalMoves:
        board[i[2]][i[3]] = board[i[0]][i[1]]
        board[i[0]][i[1]] = ''
        algScore = algorithm(depth - 1, board, -float('inf'), float('inf'), False, white, totalMoves)
        
        
        if algScore[0] > bestScore:
            bestScore = algScore[1]
            bestMove = i
            bestDepth = algScore[1]
            movesList = []
            movesList.append(bestMove)
        elif algScore[0] == bestScore:
            if algScore[1] < bestDepth:
                bestScore = algScore[1]
                bestMove = i
                bestDepth = algScore[1]
                
            #movesList.append(i)
        #print(algScore, movesList)
        board[i[0]][i[1]] = board[i[2]][i[3]]
        board[i[2]][i[3]] = i[4]

    # if len(movesList) == 1:

    board[bestMove[2]][bestMove[3]] = board[bestMove[0]][bestMove[1]]
    board[bestMove[0]][bestMove[1]] = ''
    currentPiece = board[bestMove[2]][bestMove[3]]
    currentPiece.row = bestMove[2]
    currentPiece.cell = bestMove[3] 
    oldPos = bestMove[0], bestMove[1]
    # else:
    #     move = random.randint(0, len(movesList) - 1)
    #     board[movesList[move][2]][movesList[move][3]] = board[movesList[move][0]][movesList[move][1]]
    #     board[movesList[move][0]][movesList[move][1]] = ''
    #     currentPiece = board[movesList[move][2]][movesList[move][3]]
    #     currentPiece.row = movesList[move][2]
    #     currentPiece.cell = movesList[move][3]
    #     oldPos = movesList[move][0], movesList[move][1]

    currentPiece.hasMoved = True
    
    return white

def game():
    global currentPiece, oldPos, positions, boards
    gameOver = False
    board = Board()
    
    board.setUpBoard()
    isMouseDown = False
    turn = white
    gameTurn = 0
    moves = []
    shouldDraw = False
    turns = 0
    castleSquareWhiteRight = [-2, -2]
    castleSquareWhiteLeft = [-2, -2]
    castleSquareBlackRight = [-2, -2]
    castleSquareBlackLeft = [-2, -2]
    totalMoves = []
    castling = False
    while not gameOver:
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                
                if not isMouseDown:
                    
                    if board.board[pos[1] // tileSize][pos[0] // tileSize] != '' and board.board[pos[1] // tileSize][pos[0] // tileSize].color == turn:
                        # for i in range(8):
                        #     print(board.board[7][i])
                        # print("_____________________________")
                        # print("INDICATOR 1")
                        # for i in range(8):
                        #     print(board.board[1][i])
                        
                        board.board[pos[1] // tileSize][pos[0] // tileSize].isLifted = True
                        #print(board.board[pos[1] // tileSize][pos[0] // tileSize].piece)
                        #print(board.board[pos[1] // tileSize][pos[0] // tileSize].color,)
                        moves = legalMoves(
                            board.board,
                            board.board[pos[1] // tileSize][pos[0] // tileSize].piece, 
                            board.board[pos[1] // tileSize][pos[0] // tileSize].color,
                            gameTurn,
                            pos[1] // tileSize,
                            pos[0] // tileSize,
                            board.board[pos[1] // tileSize][pos[0] // tileSize].hasMoved,
                            True
                        )
                        #print(moves)
                        #print("H")
                        #print(moves)
                        castling = False
                        #print(pos[1] // tileSize, pos[0] // tileSize)
                        currentPiece = board.board[pos[1] // tileSize][pos[0] // tileSize]
                        # for i in range(8):
                        #     for x in range(8):
                        #         if board.board[i][x] == '':
                        #             print("Empty")
                        #         else:
                        #             print(board.board[i][x])
                        #print("_____________________________")
                        if currentPiece.piece == 'King' and currentPiece.color == white and currentPiece.hasMoved == False:
                            moves, castleSquareWhiteRight = castleRightWhite(board.board, moves, gameTurn)
                            moves, castleSquareWhiteLeft = castleLeftWhite(board.board, moves, gameTurn)
                            castling = True
                        elif currentPiece.piece == 'King' and currentPiece.color == black and currentPiece.hasMoved == False:
                            moves, castleSquareBlackRight = castleRightBlack(board.board, moves, gameTurn)
                            moves, castleSquareBlackLeft = castleLeftBlack(board.board, moves, gameTurn)
                            castling = True
                        oldPos = [pos[1] // tileSize, pos[0] // tileSize]
                        shouldDraw = True
                        #print(currentPiece.color)

                        # for i in range(2, 6):
                        #     print(board.board[i])
                        
                        # print("______________________________________")

                        isMouseDown = True
                else:
                    #print(moves)
                    #print(pos[1] // tileSize, pos[0] // tileSize, oldPos)
                    if (currentPiece.row != oldPos[0] or currentPiece.cell != oldPos[1]) and (pos[1] // tileSize, pos[0] // tileSize) in moves:
                        
                        board.board[currentPiece.row][currentPiece.cell] = currentPiece
                        board.board[oldPos[0]][oldPos[1]] = ''
                        totalMoves.append((currentPiece.cell, currentPiece.row))
                        # for line in chessBook:
                        #     chars = line.split()
                        #     if len(chars[0]) == 2:
                        #         # print(boardNumberDict[totalMoves[0][1]], chars[0][1:2])
                                
                        #         # if int(boardNumberDict[totalMoves[0][1]]) == int(chars[0][1:2]):
                        #         #     print("FEIUOFNEUIFB")
                            
                        #         #print(totalMoves[0][0], totalMoves[0][1], "BREAK", totalMoves[0][0], boardLetterDict[chars[0][:1]], int(boardNumberDict[totalMoves[0][1]]), int(chars[0][1:2]))
                        #         if totalMoves[0][0] == boardLetterDict[chars[0][:1]] and int(boardNumberDict[totalMoves[0][1]]) == int(chars[0][1:2]):
                        #             #print("Hello")
                        #             print(chars[0])
                        #         #pygame.time.delay(20000)
                        if castling: 
                            board.board = castle(currentPiece.row, currentPiece.cell, castleSquareWhiteRight, castleSquareWhiteLeft, castleSquareBlackRight, castleSquareBlackLeft, board.board)
                        # if isKingInCheck(white, board.board, gameTurn):
                        #     print("White King in Check!")
                        # if isKingInCheck(black, board.board, gameTurn):
                        #     print("Black King in Check")
                        otherTurn = white if turn == black else black
                        if checkMate(otherTurn, board.board, gameTurn):
                            print("MATE")
                        currentPiece.hasMoved = True
                        turn = black if turn == white else white
                        
                        # when gameTurn is 1 that means black and white have played
                        gameTurn += 0.5

                    else:
                        currentPiece.row = oldPos[0]
                        currentPiece.cell = oldPos[1]
                    shouldDraw = False

                    #elif board.board[pos[1] // tileSize][pos[0] // tileSize] == '':


                    currentPiece.isLifted = False
                    #moves = []
                    # for i in range(2, 6):
                    #         print(board.board[i])
                        
                    # print("______________________________________")

                   
                    
                    isMouseDown = False

    
        board.drawBoard()

        if shouldDraw:
            for i in moves:
                pygame.draw.circle(window, red, ((i[1] * tileSize) + (tileSize // 2), (i[0] * tileSize) + (tileSize // 2)), 5)

        if oldPos != None and currentPiece != None:
            pygame.draw.rect(window, lightGreen, (oldPos[1] * tileSize, oldPos[0] * tileSize, tileSize, tileSize))
            pygame.draw.rect(window, turqoise, (currentPiece.cell * tileSize, currentPiece.row * tileSize, tileSize, tileSize))
        
        for row in board.board:
            for cell in row:
                if cell != "" and cell != currentPiece:
                    cell.draw()

        if currentPiece != None:
            currentPiece.draw()
        
        
        totalMoves = []

        for row in board.board:
            for cell in row:
                if cell != "":


                    if cell.isLifted and (pos[1] // tileSize, pos[0] // tileSize) in moves:
                        cell.row = pos[1] // tileSize
                        cell.cell = pos[0] // tileSize



        if turn == black:
            turn = pickMove(board.board, turn, 3)
            print(positions)
            #print(boards)
            positions = 0
            boards = []
        '''
        if turn == black:
            bestScore = -(float('inf'))
            bestMove = None
            #pygame.time.delay(500)
            # for i in range(8):
            #     for x in range(8):
            #         if board.board[i][x] != '':
            #             print(board.board[i][x].piece, end=' ')
            #         else:
            #             print("Empty", end = ' ')

            # print("____________________________________-")
            generateAllMoves(turn, board.board)

            for i in totalMoves:
                board.board[i[2]][i[3]] = board.board[i[0]][i[1]]
                board.board[i[0]][i[1]] = ''
                score = evaluateBoard(board.board)
                if score > bestScore:
                    bestScore = score
                    bestMove = i
                board.board[i[0]][i[1]] = board.board[i[2]][i[3]]
                board.board[i[2]][i[3]] = i[4]

            board.board[bestMove[2]][bestMove[3]] = board.board[bestMove[0]][bestMove[1]]
            board.board[bestMove[0]][bestMove[1]] = ''
            currentPiece = board.board[bestMove[2]][bestMove[3]]
            currentPiece.row = bestMove[2]
            currentPiece.cell = bestMove[3]
            turn = white
            

            #print(totalMoves)
            #print("_____________________________________")  
            #print(len(totalMoves))

            #pygame.time.delay(50000)
            '''
        promote(board.board)
        # if turns % 200 == 0:
        #     for i in range(2, 6):
        #         print(board.board[i])

        #     print("_______________________________")
        
        turns += 1
        pygame.display.update()

if __name__ == '__main__':  
    game()