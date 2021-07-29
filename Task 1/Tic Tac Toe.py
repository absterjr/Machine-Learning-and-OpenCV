import pygame
import sys

WIDTH = 600
HEIGHT = 600

pygame.init()
screen =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()

class Board:
    line_color = (19, 24, 97)
    board_size = 450
    # we need these two to draw the lines for the board
    start_coord = (WIDTH - board_size)//2
    end_coord = (WIDTH-start_coord)

    box_size = 450//3

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        temp_x = Board.start_coord
        temp_y = Board.start_coord
        for i in range(3):
            for j in range(3):
                self.board[i][j] = Box((temp_x, temp_y), i, j, ' ')
                temp_x += Board.box_size
            temp_x = Board.start_coord
            temp_y += Board.box_size

    def draw(self, screen):
        temp_x = Board.start_coord + Board.box_size 
        temp_y = Board.start_coord
        for _ in range(2):
            pygame.draw.line(screen, Board.line_color, (temp_x, temp_y), (temp_x, Board.end_coord), 5)
            temp_x += Board.box_size
        
        temp_x = Board.start_coord
        temp_y = Board.start_coord + Board.box_size
        for _ in range(2):
            pygame.draw.line(screen, Board.line_color, (temp_x, temp_y), (Board.end_coord, temp_y), 5)
            temp_y += Board.box_size

    def checkForWin(self, turn):
        for i in range(3):
            for j in range(3):
                if self.board[i][j].val != turn:
                    break
            else:
                return True
        
        for i in range(3):
            for j in range(3):
                if self.board[j][i].val != turn:
                    break
            else:
                return True
        
        if self.board[1][1].val == turn and self.board[2][0].val == turn and self.board[0][2].val == turn:
            return True

        if self.board[1][1].val == turn and self.board[0][0].val == turn and self.board[2][2].val == turn:
            return True

        return False

class Box:
    padding = 30

    def __init__(self, pos, i, j, val):
        self.val = val
        self.pos = pos
        self.x, self.y = pos
        self.i = i
        self.j = j
        self.rect = pygame.Rect(self.x, self.y, Board.box_size, Board.box_size)
        self.center = self.rect.center
    
    def draw(self, screen):
        if self.val == 'X':
            pygame.draw.line(screen, (247, 170, 0), (self.x + Box.padding, self.y + Box.padding), (self.x + Board.box_size - Box.padding, self.y + Board.box_size - Box.padding), 5)
            pygame.draw.line(screen, (247, 170, 0), (self.x + Box.padding, self.y + Board.box_size - Box.padding), (self.x + Board.box_size - Box.padding, self.y + Box.padding), 5)
        if self.val == 'O':
            pygame.draw.circle(screen, (0,255,0), self.center, (Board.box_size - (2 * Box.padding))/2, 5)

    def eventHandler(self, event, val):
        if self.rect.collidepoint(event.pos):
            print("Coordinates:" ,self.i, self.j)
            if self.val == ' ':
                self.val = val
                return True

def main():
    b = Board()
    turn = 'X'
    move_count = 0
    game = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in range(3):
                            for j in range(3):
                                if b.board[i][j].eventHandler(event, turn):
                                    #if move was succesful change the player
                                    if b.checkForWin(turn):
                                        game = False
                                    if turn == 'X':
                                        turn = 'O'
                                    else:
                                        turn = 'X'
                                    move_count += 1
                                    if move_count == 9:
                                        turn = ' '
                                        game = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        game = True
                        b = Board()
        
        screen.fill((84, 92, 235))
        if game == False:
            if turn == 'X':
                pygame.draw.circle(screen, (0,255,0), (WIDTH/2, 150), 100, 10)
            elif turn == 'O':
                pygame.draw.line(screen, (247, 170, 0), (200,100), (400,300), 10)
                pygame.draw.line(screen, (247, 170, 0), (200,300), (400,100), 10)
            else:
                pygame.draw.circle(screen, (0,255,0), (150, 200), 100, 10)
                pygame.draw.line(screen, (247, 170, 0), (300,100), (500,300), 10)
                pygame.draw.line(screen, (247, 170, 0), (300,300), (500,100), 10)
        else:
            b.draw(screen)
            for i in range(3):
                for j in range(3):
                    b.board[i][j].draw(screen)
        pygame.display.update()
        clock.tick()

if __name__ == '__main__':
    main()