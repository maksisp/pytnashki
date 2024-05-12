import pygame

def win_menu(screen, moves):
    screen.fill((255, 255, 255))
    font_title = pygame.font.Font(None, 50)
    font_text = pygame.font.Font(None, 36)

    text_title = font_title.render("Поздравляем!", True, (0, 0, 0))
    text_title_rect = text_title.get_rect(center=(200, 100))
    screen.blit(text_title, text_title_rect)

    text_moves = font_text.render(f"Количество ходов: {moves}", True, (0, 0, 0))
    text_moves_rect = text_moves.get_rect(center=(200, 200))
    screen.blit(text_moves, text_moves_rect)

    return_button = pygame.Rect(100, 300, 200, 50)
    pygame.draw.rect(screen, (0, 0, 0), return_button, 2)

    text_return = font_text.render("Выход", True, (0, 0, 0))
    text_return_rect = text_return.get_rect(center=return_button.center)
    screen.blit(text_return, text_return_rect)

    pygame.display.update()
    return return_button