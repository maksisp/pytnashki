import pygame
from game import random_board, check_win, find_empty_square
from mainmenu import main_menu
import sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Пятнашки")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


game_board =  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, ' '], [13, 14, 15, 12]] # проверка проверки на победу
#game_board = random_board()

moves = 0
game_active = True
pygame.mixer.music.set_volume(0.2)
move_sound = pygame.mixer.Sound('./sounds/свайп.mp3')
reload_sound = pygame.mixer.Sound('./sounds/reload.wav')
victory_sound = pygame.mixer.Sound('./sounds/victory.mp3')
pygame.mixer.music.load('./sounds/фон.mp3')
pygame.mixer.music.play(-1)


def run_game(initial_board):
    game_board = initial_board
    moves = 0
    game_active = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and game_active:
                x, y = event.pos
                i, j = y // 100, x // 100
                empty_i, empty_j = find_empty_square(game_board)
                if (abs(i - empty_i) == 1 and j == empty_j) or (abs(j - empty_j) == 1 and i == empty_i):
                    if 0 <= i < 4 and 0 <= j < 4:
                        game_board[i][j], game_board[empty_i][empty_j] = game_board[empty_i][empty_j], game_board[i][j]
                        move_sound.play()
                        moves += 1

        if check_win(game_board):
            victory_sound.set_volume(0.3)
            victory_sound.play()
            font = pygame.font.Font(None, 36)
            text = font.render("Вы выиграли!!!!", True, red)
            text_rect = text.get_rect(center=(200, 200))
            screen.blit(text, text_rect)
            game_active = False
        pygame.display.update()

        screen.fill(white)

        for i in range(4):
            for j in range(4):
                if game_board[i][j] != ' ':
                    pygame.draw.rect(screen, (0, 0, 255), (j * 100, i * 100, 100, 100), 1)
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(game_board[i][j]), True, black)
                    text_rect = text.get_rect(center=(j * 100 + 50, i * 100 + 50))
                    screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Ходы: {moves}", True, black)
        text_rect = text.get_rect(center=(200, 450))
        screen.blit(text, text_rect)

        pygame.display.update()


main_menu_active = True
while main_menu_active:
    start_button, exit_button = main_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu_active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                main_menu_active = False
                run_game(game_board)
            elif exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

pygame.quit()
