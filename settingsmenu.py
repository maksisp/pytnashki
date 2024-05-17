import pygame

def settings_menu(screen,music_filled,sound_filled):

    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Настройки", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 50))
    screen.blit(text, text_rect)

    button_width = 200
    button_height = 50

    back_button = pygame.Rect(100, 400, button_width, button_height)
    pygame.draw.rect(screen, (0, 0, 0), back_button, 2)
    text = font.render("Назад", True, (0, 0, 0))
    text_rect = text.get_rect(center=back_button.center)
    screen.blit(text, text_rect)


    font_small = pygame.font.Font(None, 36)
    text = font_small.render("Фоновая музыка...................", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 130))
    screen.blit(text, text_rect)

    music_mark = pygame.Rect(350,130, 20, 20)
    if music_filled:
        pygame.draw.rect(screen, (252, 176, 52), music_mark, 2)
    else:
        pygame.draw.rect(screen, (252, 176, 52), music_mark)
        pygame.draw.rect(screen, (0,0,0), music_mark, 2)


    font_small = pygame.font.Font(None, 36)
    text = font_small.render("Звуки......................................", True, (0, 0, 0))
    text_rect = text.get_rect(topleft=(10, 170))
    screen.blit(text, text_rect)

    sound_mark = pygame.Rect(350,170, 20, 20)
    if sound_filled:
        pygame.draw.rect(screen, (252, 170, 52), sound_mark, 2)
    else:
        pygame.draw.rect(screen, (252, 176, 52), sound_mark)
        pygame.draw.rect(screen, (0,0,0), sound_mark, 2)
    pygame.display.update()
    return back_button, music_mark, sound_mark