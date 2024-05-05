import pygame

screen = pygame.display.set_mode((400, 500))

def main_menu():
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 50)
    text = font.render("Главное меню", True, (0,0,0))
    text_rect = text.get_rect(center=(200, 200))
    screen.blit(text, text_rect)

    start_button = pygame.Rect(150, 300, 100, 50)
    pygame.draw.rect(screen, (255,0,0), start_button)
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, (0,0,0))
    text_rect = text.get_rect(center=start_button.center)
    screen.blit(text, text_rect)

    pygame.display.update()
    return start_button



#white = (255, 255, 255)
#black = (0, 0, 0)
#red = (255, 0, 0)