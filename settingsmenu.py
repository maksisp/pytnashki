import pygame

def settings_menu(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Настройки", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 200))
    screen.blit(text, text_rect)

    button_width = 200
    button_height = 50

    back_button = pygame.Rect(100, 320, button_width, button_height)
    pygame.draw.rect(screen, (0, 0, 0), back_button, 2)
    text = font.render("Назад", True, (0, 0, 0))
    text_rect = text.get_rect(center=back_button.center)
    screen.blit(text, text_rect)

    pygame.display.update()
    return back_button