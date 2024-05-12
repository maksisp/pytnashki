import pygame

screen = pygame.display.set_mode((400, 500))

def main_menu(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Пятнашки", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 200))
    screen.blit(text, text_rect)

    button_width = 200
    button_height = 50

    start_button = pygame.Rect(100, 250, button_width, button_height)
    pygame.draw.rect(screen, (0, 0, 0), start_button, 2)
    text = font.render("Старт", True, (0, 0, 0))
    text_rect = text.get_rect(center=start_button.center)
    screen.blit(text, text_rect)

    settings_button = pygame.Rect(100, 320, button_width, button_height)
    pygame.draw.rect(screen, (0, 0, 0), settings_button, 2)
    text = font.render("Настройки", True, (0, 0, 0))
    text_rect = text.get_rect(center=settings_button.center)
    screen.blit(text, text_rect)

    exit_button = pygame.Rect(100, 390, button_width, button_height)
    pygame.draw.rect(screen, (0, 0, 0), exit_button, 2)
    text = font.render("Выход", True, (0, 0, 0))
    text_rect = text.get_rect(center=exit_button.center)
    screen.blit(text, text_rect)

    
    pygame.display.update()
    return start_button, settings_button, exit_button


#white = (255, 255, 255)
#black = (0, 0, 0)
#red = (255, 0, 0)