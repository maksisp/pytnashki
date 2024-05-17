# main.py
import pygame
from game import random_board, check_win, find_empty_square
from mainmenu import main_menu
from settingsmenu import settings_menu
from winmenu import win_menu
import sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Пятнашки")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#game_board =  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, ' '], [13, 14, 15, 12]] # проверка проверки на победу
game_board = random_board()
save_board =  [[]]

win_count = 0
moves = 0
saved = 0
game_active = True
pygame.mixer.music.set_volume(0.2)
move_sound = pygame.mixer.Sound('./sounds/свайп.mp3')
reload_sound = pygame.mixer.Sound('./sounds/reload.wav')
victory_sound = pygame.mixer.Sound('./sounds/victory.mp3')
pygame.mixer.music.load('./sounds/фон.mp3')
pygame.mixer.music.play(-1)

def run_game(game_board):
    global main_menu_active , moves , win_count , saved , save_board
    game_active = True
    
    if win_count == 1:
        game_board = random_board()
        #game_board =  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, ' '], [13, 14, 15, 12]] # проверка проверки на победу
        win_count = 0 
    
    if saved == 1:
        game_board = save_board
        saved = 0
        


        

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and game_active:
                x, y = event.pos
                i, j = y // 100, x // 100
                empty_i, empty_j = find_empty_square(game_board)
                if (abs(i - empty_i) == 1 and j == empty_j) or (abs(j - empty_j) == 1 and i == empty_i):
                    if 0 <= i < 4 and 0 <= j < 4:
                        game_board[i][j], game_board[empty_i][empty_j] = game_board[empty_i][empty_j], game_board[i][j]
                        move_sound.play()
                        moves += 1
                     
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_board = random_board()
                    reload_sound.play()
                    moves = 0
                    game_active = True
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_ESCAPE:
                    save_board = game_board
                    saved = 1
                    running = False
                    main_menu_active = True
                    
                    

                   
            if check_win(game_board) and win_count < 1:
                running = False
                victory_sound.set_volume(0.3)
                victory_sound.play()
                win_menu_button = win_menu(screen, moves) 
                win_count =  1
                win_menu_active = True
                moves = 0
                while win_menu_active:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if win_menu_button.collidepoint(event.pos):
                                running = False
                                win_menu_active = False
                                main_menu_active = True
                                
                            
        
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


def run_settings():
    global main_menu_active
    music_on = True
    settings_menu_active = True 
    while settings_menu_active:
        back_button, music_on_button, music_off_button = settings_menu(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    settings_menu_active = False
                    main_menu_active = True
                elif music_on_button.collidepoint(event.pos):
                    if not music_on:
                        pygame.mixer.music.play(-1)
                        music_on = True
                elif music_off_button.collidepoint(event.pos):
                    if music_on:
                        pygame.mixer.music.stop()
                        music_on = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_menu_active = False
                    main_menu_active = True

main_menu_active = True
while main_menu_active:
    start_button, settings_button, exit_button = main_menu(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                main_menu_active = False
                run_game(game_board)
            elif exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
            elif settings_button.collidepoint(event.pos):
                run_settings()

pygame.quit()
