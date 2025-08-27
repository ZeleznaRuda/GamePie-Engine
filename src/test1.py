import pygame
pygame.init()

screen = pygame.display.set_mode((500, 200))
pygame.display.set_caption("Fonty v Arch Linux")

# Načtení systémového fontu
font = pygame.font.SysFont("DejaVu Sans", 40)  

text_surface = font.render("Ahoj, Arch!", True, (255, 255, 255))
screen.blit(text_surface, (50, 50))
pygame.display.flip()

# Hlavní smyčka
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
