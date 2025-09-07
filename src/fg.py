import pygame

pygame.init()
info = pygame.display.Info()
surface = pygame.display.set_mode((info.current_w, info.current_h))
pygame.display.set_caption("Maximized")

# --- smyčka hry ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill((100, 150, 200))
    pygame.display.flip()

pygame.quit()
