import pygame
from ..surface import Surface


def rect(surface, color=(255, 255, 255), width=0, border_radius=0,
         border_top_left_radius=0, border_top_right_radius=0,
         border_bottom_left_radius=0, border_bottom_right_radius=0,
         rect=None, angle=0, flip=(False,False)):
    surface = surface()
    

    if rect is None:
        rect = (0, 0, 60, 50)
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        raise ValueError("Cannot scale to non-positive size")


    temp = Surface((w, h))
    pygame.draw.rect(
        temp(), color, (0, 0, w, h), width=width,
        border_radius=border_radius,
        border_top_left_radius=border_top_left_radius,
        border_top_right_radius=border_top_right_radius,
        border_bottom_left_radius=border_bottom_left_radius,
        border_bottom_right_radius=border_bottom_right_radius
    )
    if flip != (False, False):
        temp = temp.transform.flip(*flip)

    if angle != 0:
        rotated = temp.transform.rotate(angle)
        rotated_rect = rotated.rect
        rotated_rect.center = (x + w // 2, y + h // 2)
        surface.blit(rotated(), rotated_rect.topleft)
    else:
        surface.blit(temp(), (x, y))


def ellipse(surface, color=(255, 255, 255), width=0, rect=None, flip=(False,False), angle=0):
    surface = surface()
    if rect is None:
        rect = (0, 0, 60, 50)
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        raise ValueError("Cannot scale to non-positive size")

    temp = Surface((w, h))
    pygame.draw.ellipse(temp(), color, (0, 0, w, h), width=width)
    if flip != (False, False):
        temp = temp.transform.flip(*flip)
    if angle != 0:
        rotated = temp.transform.rotate(angle)
        rotated_rect = rotated.rect
        rotated_rect.center = (x + w // 2, y + h // 2)
        surface.blit(rotated(), rotated_rect.topleft)
    else:
        surface.blit(temp(), (x, y))


def line(surface, color=(255, 255, 255), start_pos=None, end_pos=None, width=1,anti_aliasing=True,blend=True,  line_points=None, angle=0):
    surface = surface()
    if line_points:
        start_pos, end_pos = line_points
    if start_pos is None or end_pos is None:
        raise ValueError("You must enter start_pos and end_pos, or line_points")
    if width <= 0:
        raise ValueError("Cannot scale to non-positive size")

    min_x = min(start_pos[0], end_pos[0])
    min_y = min(start_pos[1], end_pos[1])
    max_x = max(start_pos[0], end_pos[0])
    max_y = max(start_pos[1], end_pos[1])
    w = max_x - min_x + width
    h = max_y - min_y + width

    temp = Surface((w, h))
    offset_start = (start_pos[0] - min_x, start_pos[1] - min_y)
    offset_end = (end_pos[0] - min_x, end_pos[1] - min_y)

    if anti_aliasing:
        pygame.draw.aaline(temp(), color, offset_start, offset_end, blend=blend)
    elif not anti_aliasing:
        pygame.draw.line(temp(), color, offset_start, offset_end, width)

    if angle != 0:
        rotated = temp.transform.rotate(angle)
        rotated_rect = rotated.rect
        rotated_rect.center = ((min_x + max_x) // 2, (min_y + max_y) // 2)
        surface.blit(rotated(), rotated_rect.topleft)
    else:
        surface.blit(temp(), (min_x, min_y))

def label(surface, text,font, color=(255, 255, 255),background_color=(255,255,255),anti_aliasing=True,rect=None):
    surface = surface()
    if rect is None:
        rect = (0, 0, 60, 50)
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        raise ValueError("Cannot scale to non-positive size")

    temp = Surface((w, h))
    font = font()
    text = font.render(text, anti_aliasing, color,background_color)
    surface.blit(text, (x, y))

def image(surface, image, color=(255, 255, 255), rect=None, angle=0,flip=(False,False), tint_mode="multiply"):
    # //ai
    def _ensure_wrapper(surf):
        if isinstance(surf, Surface):
            return surf
        elif isinstance(surf, pygame.Surface):
            return Surface(surface=surf)
        else:
            raise TypeError(f"Cannot wrap object of type {type(surf)} as Surface")
    target = surface()
    target = _ensure_wrapper(target)

    if rect is None:
        rect = (0, 0, 60, 50)
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        raise ValueError("Cannot scale to non-positive size")

    raw = image()
    raw = _ensure_wrapper(raw)
    temp = raw.copy()

    if color != (255, 255, 255):
        if tint_mode == "multiply":
            tint = Surface(size=temp.size, flags=[pygame.SRCALPHA])
            tint.fill(color)
            temp().blit(tint(), (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        elif tint_mode == "overlay":
            overlay = Surface(size=temp.size, flags=[pygame.SRCALPHA])
            r, g, b = color
            overlay.fill((r, g, b, 127))
            temp().blit(overlay(), (0, 0))
        else:
            pass 

    if flip != (False, False):
        temp = temp.transform.flip(*flip)
    scaled = temp.transform.scale((w, h))


    if angle != 0:
        rotated = scaled.transform.rotate(angle)
        rotated_rect = rotated.rect
        rotated_rect.center = (x + w // 2, y + h // 2)
        target.blit(rotated(), (rotated_rect.x, rotated_rect.y))
    else:
        target.blit(scaled(), (x, y))
