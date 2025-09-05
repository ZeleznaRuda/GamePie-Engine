_type = "gpinfo"
_msg = "Error: Something went wrong!\nPlease try again."
import subprocess

import platform
import pygame

pygame.mixer.init()  # Inicializace audio modulu
pygame.mixer.music.load("src/gamepie/assets/msgIco/music-box-336285.mp3")  # Načtení souboru
pygame.mixer.music.play()  # Přehrání

def get_system_theme():
    # ai
    system = platform.system()
    
    # Windows
    if system == "Windows":
        try:
            import winreg
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return "Light" if value == 1 else "Dark"
        except:
            return "Unknown"

    # macOS
    elif system == "Darwin":
        try:
            result = subprocess.run(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                capture_output=True, text=True
            )
            return "Dark" if "Dark" in result.stdout else "Light"
        except:
            return "Light"  # pokud není nastaveno tmavé téma

    # Linux
    elif system == "Linux":

        try:
            # GNOME
            result = subprocess.run(
                ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
                capture_output=True, text=True
            )
            output = result.stdout.strip().lower()
            if "dark" in output:
                return "Dark"
            elif "light" in output:
                return "Light"
        except:
            pass

        try:
            # Cinnamon / Manjaro
            result = subprocess.run(
                ["gsettings", "get", "org.cinnamon.desktop.interface", "gtk-theme"],
                capture_output=True, text=True
            )
            theme = result.stdout.strip().strip("'").lower()
            if "dark" in theme:
                return "Dark"
            else:
                return "Light"
        except:
            pass

        return "Unknown"

    else:
        return "Unknown"

# Příklad použití
theme = get_system_theme()


import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.config(bg="#f0f0f0" if theme == "Light" else "#2e2e2e")
img = Image.open("src/gamepie/assets/msgIco/gperr.png")
if _type == "gperror":
    root.title("Error Message Box")
    img = Image.open("src/gamepie/assets/msgIco/gperr.png")
if _type == "gpwarn":
    root.title("Warning Message Box")
    img = Image.open("src/gamepie/assets/msgIco/gpwarn.png")
if _type == "gpmsg":
    root.title("Message Box")
    img = Image.open("src/gamepie/assets/msgIco/gpmsg.png")
if _type == "gpquest":
    root.title("Question Message Box")
    img = Image.open("src/gamepie/assets/msgIco/gpquest.png")
if _type == "gpinfo":
    root.title("Information Message Box")
    img = Image.open("src/gamepie/assets/msgIco/gpinfo.png")
img = img.resize((100, 100)) 
photo = ImageTk.PhotoImage(img)

label = tk.Label(
    root,
    image=photo,
    text=_msg,
    compound="left",   
    font=("Arial", 12),
    anchor="nw",       
    justify="left"      
)
label.config(bg="#f0f0f0" if theme == "Light" else "#2e2e2e", fg="#000000" if theme == "Light" else "#ffffff")
label.pack(padx=10, pady=10, fill="both")
root.resizable(False, False)
root.mainloop()
