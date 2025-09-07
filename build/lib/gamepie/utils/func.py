import sys
import pygame
import platform
import os
import subprocess
import inspect

def get_mypath():
    frame = inspect.stack()[1]
    caller_file = frame.filename
    return os.path.abspath(caller_file)
from ..core import _gp_log
        
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
    from ..pather import BASE_DIR
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

def venv_start(name=None):
    if name is None:
        name = "main"  # nebo get_mypath(), podle toho co máš

    if platform.system() == "Windows":
        python_exe = os.path.join("venv", "Scripts", "python.exe")
    else:
        python_exe = os.path.join("venv", "bin", "python")

    subprocess.run([python_exe, f"{name}.py"])

def screenshot(surface, name=f"screenshot.jpg", msg=True):
    from .gpbox import Messagebox as msgbox
    surface = surface()
    pygame.image.save(surface, name)
    if msg:
        msgbox(f"Screenshot was save in \n'{name}' .").show(type=61)


def gpdata_save(objects, filename="objects.dat"):
    import pickle
    import json
    data = []

    for obj in objects:
        if isinstance(obj, dict):
            obj_data = obj.copy()
        else:
            obj_data = {}
            obj_data.update(obj.__dict__)
            # uložíme i properties
            for name, attr in inspect.getmembers(type(obj), lambda o: isinstance(o, property)):
                try:
                    obj_data[name] = getattr(obj, name)
                except Exception:
                    pass
            obj_data['_class'] = type(obj).__name__

        data.append(obj_data)

    ext = os.path.splitext(filename)[1].lower()
    try:
        if ext == ".json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        else:  # pickle jako default
            with open(filename, "wb") as f:
                pickle.dump(data, f)
        _gp_log(f"objects saved to '{filename}'")
    except Exception as e:
        _gp_log(f"[fatal error]: could not save objects '{e}'")


def gpdata_load(filename="objects.dat"):
    import pickle
    import json
    if not os.path.exists(filename):
        _gp_log("no saved file found.")
        return []

    if os.path.getsize(filename) == 0:
        _gp_log("saved file is empty.")
        return []

    ext = os.path.splitext(filename)[1].lower()
    try:
        if ext == ".json":
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:  # pickle
            with open(filename, "rb") as f:
                data = pickle.load(f)
        _gp_log(f"objects loaded from '{filename}'")
        return data
    except (json.JSONDecodeError, EOFError, Exception) as e:
        _gp_log(f"[fatal error]: file corrupted or invalid: {e}")
        return []

def build(script_path: str, icon=None, windowed=False, output_dir=None):
    import subprocess
    from pathlib import Path
    import platform
    from ..pather import paths, ICON70
    from ..core import _gp_log

    script_path = Path(script_path).resolve()
    sep = ";" if platform.system() == "Windows" else ":"
    base_dir = Path(__file__).resolve().parent
    assets_dir = base_dir / "assets"
    plugins_dir = base_dir / "plugins"

    if not assets_dir.exists():
        print("[build]: 'assets' folder not found!")
        return

    if icon is None:
        icon = ICON70

    if output_dir is None:
        output_dir = script_path.parent
    else:
        output_dir = Path(output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

    def collect_add_data(folder: Path, target_name: str):
        items = []
        for path in folder.rglob("*"):
            if path.is_file():
                rel_path = path.relative_to(folder)
                items.append(f"{path}{sep}{target_name}/{rel_path.parent.as_posix()}")
        return items

    add_data = collect_add_data(assets_dir, "assets") + collect_add_data(plugins_dir, "plugins")

    command = [
        "pyinstaller",
        "--onefile",
        f"--distpath={output_dir}",
        str(script_path)
    ]

    if icon:
        command.append(f"--icon={icon}")
    if windowed:
        command.append("--noconsole")
    for data in add_data:
        command.append(f"--add-data={data}")

    _gp_log("[build]: running PyInstaller...")
    _gp_log("[build]: command:" + " ".join(command))

    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        _gp_log("[build]: PyInstaller finished with an error!")
    else:
        _gp_log("[build]: Build completed successfully!")

  
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