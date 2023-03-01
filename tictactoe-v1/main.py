# 01-03-23
import pygame, sys
import tictactoe as ttt

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
TILE_SIZE = 80
board = ttt.initial_state()
tiles = []

def draw_board():
    tile_origin = (SCREEN_WIDTH / 2 - (1.5 * TILE_SIZE), SCREEN_HEIGHT / 2 - (1.5 * TILE_SIZE))
    tiles.clear()
    for i in range(3):
        rows = []
        for j in range(3):
            rect = pygame.Rect(
                tile_origin[0] + j * TILE_SIZE,
                tile_origin[1] + i * TILE_SIZE,
                TILE_SIZE, TILE_SIZE
            )

            pygame.draw.rect(screen, 'white', rect, 3)

            if board[i][j] is not None:
                move = medium_font.render(board[i][j], True, 'white')
                move_rect = move.get_rect()
                move_rect.center = rect.center
                screen.blit(move, move_rect)

            rows.append(rect)

        tiles.append(rows)

def move():
    if pygame.mouse.get_pressed()[0] and not ttt.terminal(board):
        mouse = pygame.mouse.get_pos()

        for i in range(3):
            for j in range(3):
                if (board[i][j] is None and tiles[i][j].collidepoint(mouse)):
                    return ttt.result(board, (i, j))

    return board

small_font = pygame.font.SysFont(None, 32)
medium_font = pygame.font.SysFont(None, 48)
large_font = pygame.font.SysFont(None, 72)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    board = move()
    draw_board()
    pygame.display.flip()
    
