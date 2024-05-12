import pygame

def settings_menu(screen):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Settings", True, (0, 0, 0))
    text_rect = text.get_rect(center=(200, 200))
    screen.blit(text, text_rect)

    back_button = pygame.Rect(150, 380, 100, 50)
    pygame.draw.rect(screen, (255, 0, 0), back_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Back", True, (0, 0, 0))
    text_rect = text.get_rect(center=back_button.center)
    screen.blit(text, text_rect)

    pygame.display.update()
    return back_button