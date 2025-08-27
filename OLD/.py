import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Pozice objektu (střed)
x, y = WIDTH // 2, HEIGHT // 2

# Vytvoříme jednoduchý povrch: trojúhelník směřující "nahoru"
base_surf = pygame.Surface((60, 80), pygame.SRCALPHA)
pygame.draw.polygon(
    base_surf,
    (200, 100, 50),
    [(30, 0), (0, 80), (60, 80)]  # špička nahoře
)
orig_rect = base_surf.get_rect(center=(x, y))

def rotate_center(surf, angle, center):
    """Otočí surf a vrátí nový surf i rect zarovnaný na dané centrum."""
    rotated = pygame.transform.rotozoom(surf, angle, 1)  # otočení proti směru hodinových ručiček
    new_rect = rotated.get_rect(center=center)
    return rotated, new_rect

def shortest_angle_diff(target, current):
    """Najde nejkratší rotační cestu mezi úhly ve stupních."""
    a = (target - current) % 360
    if a > 180:
        a -= 360
    return a

current_angle = 0.0  # počáteční úhel ve stupních

SMOOTHING = 0.2  # 0 = okamžitě, 1 = pomalu (čím menší, tím rychlejší natočení)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - x, my - y

    # Úhel v radiánech od středu objektu ke kurzoru (v souřadnicích Pygame y dolů)
    # Protože trojúhelník směřuje nahoru, odečteme 90 stupňů, aby špička směřovala k cíli.
    target_angle = math.degrees(math.atan2(dy, dx)) - 90

    # Vyhlazení otočení (volitelné)
    diff = shortest_angle_diff(target_angle, current_angle)
    current_angle += diff * SMOOTHING
    current_angle %= 360

    screen.fill((30, 30, 35))

    rotated_surf, rotated_rect = rotate_center(base_surf, current_angle, (x, y))
    screen.blit(rotated_surf, rotated_rect)

    # Volitelně: vykreslit čáru od objektu ke kurzoru pro vizualizaci
    pygame.draw.line(screen, (180, 180, 180), (x, y), (mx, my), 1)
    pygame.draw.circle(screen, (255, 255, 255), (mx, my), 5)  # kurzor

    pygame.display.flip()
    clock.tick(60)
