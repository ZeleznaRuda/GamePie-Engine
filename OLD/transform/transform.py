import pygame


def rotate(surface, angle):
    return pygame.transform.rotate(surface, angle)

def scale(surface, size, scale2x=False, smoothscale=False):
    if scale2x:
        return pygame.transform.scale2x(surface)
    elif smoothscale:
        return pygame.transform.smoothscale(surface, size)
    else:
        return pygame.transform.scale(surface, size)

def rotozoom(surface, angle, scale):
    return pygame.transform.rotozoom(surface, angle, scale)

def flip(surface, flip_x, flip_y):
    return pygame.transform.flip(surface, flip_x, flip_y)

def chop(surface, rect):
    return pygame.transform.chop(surface, rect)
