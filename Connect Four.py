import pygame
import sys

from pygame import color

WIDTH = 700
HEIGHT = 650

pygame.init()
screen =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect Four')
clock = pygame.time.Clock()

class Board:
    w = 600
    h = 600
    col_w = w/7
    color = (32, 119, 250)
    start_x = (WIDTH - w)//2
    start_y = (HEIGHT - h)//2
    cols = 7
    rows = 6

    directions = [[(1,0), (-1,0)], [(0,1), (0,-1)],
                  [(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]
    def __init__(self):
        self.board = [' ' for _ in range(Board.cols)]
        self.rect = pygame.Rect(Board.start_x, Board.start_y, Board.w, Board.h)
        temp_x = Board.start_x
        for i in range(Board.cols):
            self.board[i] = Column(temp_x, i)
            temp_x += Board.col_w

    
    def draw(self, screen):
        pygame.draw.rect(screen, Board.color, self.rect)

    def checkForWin(self, i, j, turn):
        print("Coordinates: " ,i, j)
        for direction in Board.directions:
            count = 1
            for x, y in direction:
                for p in range(1, 4):
                    px = p * x
                    py = p * y
                    try:
                        if self.board[i+px].holes[j+py] == turn:
                            count += 1
                    except:
                        break

            if count == 4:
                return True
        return False

class Column:
    padding = 20
    hole_r = 40
    colors = {'red':(255,0,0), 'yellow':(255,255,0), ' ':(84, 92, 235)}
    def __init__(self, x, i):
        self.x = x
        self.i = i
        self.holes = [' ' for _ in range(Board.rows)]
        self.rect = pygame.Rect(self.x, Board.start_y, Board.col_w, Board.h)
        self.centerx = self.rect.centerx
        self.tokens_in_col = 0

    def draw(self, screen):
        temp_y = Board.start_y + Column.padding/2 + Column.hole_r
        for i in range(len(self.holes)-1, -1, -1):
            pygame.draw.circle(screen, Column.colors[self.holes[i]], (self.centerx, temp_y), Column.hole_r)
            temp_y += 2 * Column.hole_r + Column.padding

    def eventHandler(self, event, val):
        if self.rect.collidepoint(event.pos):
            if self.tokens_in_col < 6:
                if self.holes[self.tokens_in_col] == ' ':
                    self.holes[self.tokens_in_col] = val
                    self.tokens_in_col += 1
                    return True

    def getJ(self):
        return self.tokens_in_col - 1

def main():
    b = Board()       
    turn = 'yellow'    
    game = True
    move_count = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if game:
                        for i, col in enumerate(b.board):
                            if col.eventHandler(event, turn):
                                if b.checkForWin(i, col.getJ(), turn):
                                    game = False
                                if turn == 'yellow':
                                    turn = 'red'
                                else:
                                    turn = 'yellow'
                                move_count += 1
                                if move_count == 42:
                                    turn = ' '
                                    game = False
                    else:
                        game = True
                        b = Board()
        screen.fill((84, 92, 235))

        if game == False:
            if turn == 'yellow':
                pygame.draw.circle(screen, Column.colors['red'], (WIDTH/2, HEIGHT/2), 200)
            elif turn == 'red':
                pygame.draw.circle(screen, Column.colors['yellow'], (WIDTH/2, HEIGHT/2), 200)
            else:
                pygame.draw.circle(screen, Column.colors['red'], (250, 300), 150)
                pygame.draw.circle(screen, Column.colors['yellow'], (650, 300), 150)
        else:
            b.draw(screen)
            for col in b.board:
                col.draw(screen)
        pygame.display.update()
        clock.tick()
if __name__ == '__main__':
    main()