import sys
import pygame
import datetime
import os
from .pather import BASE_DIR
from . import _gp_log
        
def quit():
    _gp_log(f"program was quit")
    pygame.quit()
    sys.exit()
    
def hit_check(position,size , mouse_pos):
    x, y = position
    w, h = size
    mx, my = mouse_pos
    return x <= mx <= x + w and y <= my <= y + h

def fonts():
    with open(f"{BASE_DIR}/fonts.txt", "r", encoding="utf-8") as f:
        con = f.read()

    return con

def look(obj, target_pos, smooth: float | None = None):
    import math
    def _shortest_angle_diff(target, current):
        diff = (target - current + 180) % 360 - 180
        return diff
    tx, ty = target_pos
    dx = tx - obj.x
    dy = ty - obj.y
    desired_angle = -math.degrees(math.atan2(dy, dx)) 

    if smooth is None:
        obj.angle = desired_angle
    else:
        current = obj.angle % 360
        delta = _shortest_angle_diff(desired_angle, current)
        obj.angle = current + delta * max(0.0, min(1.0, smooth))
        
def slide(obj, start_pos, end_pos, speed=2):
    x, y = start_pos
    dx = end_pos[0] - x
    dy = end_pos[1] - y
    dist = (dx**2 + dy**2) ** 0.5

    if dist > speed:
        x += dx / dist * speed
        y += dy / dist * speed
    else:
        x, y = end_pos

    if hasattr(obj, "pos"):
        obj.pos = (x, y)

    return (x, y)

        
def blit(surface, obj, position):
    surface().blit(obj, position)

def unpackobj(obj):
    x,y = obj.pos
    w,h = obj.size
    return x,y,w,h
def screenshot(surface, name=f"screenshot.jpg"):
    surface = surface()
    pygame.image.save(surface, name)

def build(script_path: str, icon=None, windowed=False, output_dir=None):
    import subprocess
    from pathlib import Path
    import platform
    from .pather import paths, ICON70

    script_path = Path(script_path).resolve()
    sep = ";" if platform.system() == "Windows" else ":"
    base_dir = Path(__file__).resolve().parent
    assets_dir = base_dir / "assets"
    plug_dir = base_dir / "plugins"

    if not assets_dir.exists():
        _gp_log("[build]: 'assets' folder not found!")
        return

    if icon is None:
        icon = ICON70

    if output_dir is None:
        output_dir = script_path.parent
    else:
        output_dir = Path(output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

    command = [
        "pyinstaller",
        "--onefile",
        f"--add-data={assets_dir}{sep}assets",
        f"--add-data={plug_dir}{sep}plugins",
        f"--distpath={output_dir}",
        str(script_path)
    ]

    if icon:
        command.insert(1, f"--icon={icon}")

    if windowed:
        command.insert(1, "--noconsole")

    _gp_log("[build]: running PyInstaller...")
    _gp_log("[build]: command:"+" ".join(command))
    subprocess.run(command, shell=True)

  
def anchor(position=None, size=None, anchor="topleft", obj=None, reverse=False):
    # //ai
    if obj is not None:
        x = getattr(obj, "x", 0)
        y = getattr(obj, "y", 0)
        width = getattr(obj, "width", getattr(obj, "w", 0))
        height = getattr(obj, "height", getattr(obj, "h", 0))
    elif position is not None and size is not None:
        x, y = position
        width, height = size
    else:
        raise ValueError("You must provide either 'obj', or both 'position' and 'size'.")

    if not reverse:
        if anchor == "topleft":
            return x, y
        elif anchor == "topright":
            return x - width, y
        elif anchor == "bottomleft":
            return x, y - height
        elif anchor == "bottomright":
            return x - width, y - height
        elif anchor == "center":
            return x - width // 2, y - height // 2
        elif anchor == "midtop":
            return x - width // 2, y
        elif anchor == "midbottom":
            return x - width // 2, y - height
        elif anchor == "midleft":
            return x, y - height // 2
        elif anchor == "midright":
            return x - width, y - height // 2
        else:
            raise ValueError(f"Unknown anchor name: {anchor}")
    else:
        if anchor == "topleft":
            return x, y
        elif anchor == "topright":
            return x + width, y
        elif anchor == "bottomleft":
            return x, y + height
        elif anchor == "bottomright":
            return x + width, y + height
        elif anchor == "center":
            return x + width // 2, y + height // 2
        elif anchor == "midtop":
            return x + width // 2, y
        elif anchor == "midbottom":
            return x + width // 2, y + height
        elif anchor == "midleft":
            return x, y + height // 2
        elif anchor == "midright":
            return x + width, y + height // 2
        else:
            raise ValueError(f"Unknown anchor name: {anchor}")