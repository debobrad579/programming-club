# 29-03-2023
import pygame, sys, time
import ai2 as ai
import tictactoe as ttt

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400

board = ttt.initial_state()
tiles = []

pygame.init()

medium_font = pygame.font.SysFont(None, 32)
large_font = pygame.font.SysFont(None, 48)
move_font = pygame.font.SysFont(None, 72)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def draw_game_board():
    tile_size = 80
    tile_origin = (SCREEN_WIDTH / 2 - (1.5 * tile_size), SCREEN_HEIGHT / 2 - (1.5 * tile_size))
    tiles.clear()
    for i in range(3):
        row = []
        for j in range(3):
            rect = pygame.Rect(
                tile_origin[0] + j * tile_size,
                tile_origin[1] + i * tile_size,
                tile_size, tile_size
            )

            pygame.draw.rect(screen, 'white', rect, 3)

            if board[i][j] != ttt.EMPTY:
                move = move_font.render(board[i][j], True, 'white')
                move_rect = move.get_rect()
                move_rect.center = rect.center
                screen.blit(move, move_rect)

            row.append(rect)

        tiles.append(row)


def draw_header():
    if ttt.terminal(board):
        winner = ttt.winner(board)
        if winner is None:
            header = f"Game Over: Tie."
        else:
            header = f"Game Over: {winner} wins."
    else:
        header = f"{ttt.player(board)}'s Turn"

    header = large_font.render(header, True, 'white')
    title_rect = header.get_rect()
    title_rect.center = ((SCREEN_WIDTH / 2), 30)
    screen.blit(header, title_rect)


def draw_button(string, position, function):
    button = pygame.Rect(position)
    text = medium_font.render(string, True, 'black')
    text_rect = text.get_rect()
    text_rect.center = button.center
    pygame.draw.rect(screen, 'white', button)
    screen.blit(text, text_rect)

    if pygame.mouse.get_pressed()[0]:
        mouse = pygame.mouse.get_pos()
        if button.collidepoint(mouse):
            time.sleep(0.2)
            function()


def reset_board():
    global board
    board = ttt.initial_state()


def move():
    if pygame.mouse.get_pressed()[0] and not ttt.terminal(board):
        mouse = pygame.mouse.get_pos()

        for i in range(3):
            for j in range(3):
                if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                    return ttt.result(board, (i, j))

    return board


def ai_move():
    global board
    board = ttt.result(board, ai.minimax(board))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')

    draw_game_board()
    draw_header()
    if ttt.terminal(board):
        draw_button("Reset", (SCREEN_WIDTH / 3, SCREEN_HEIGHT - 65, SCREEN_WIDTH / 3, 50), reset_board)
    else:
        draw_button("AI Move", (SCREEN_WIDTH / 3, SCREEN_HEIGHT - 65, SCREEN_WIDTH / 3, 50), ai_move)
    board = move()

    pygame.display.flip()
    
