import subprocess
import platform
from ..pather import resource_path
from ..core.mixer import Sound
from ..core.load import Audio
# ai //t:my
class Messagebox:
    def __init__(self, msg, title=None):
        self._title = title
        self._msg = msg
        self.result = None  # výsledek pro tlačítka
        self.s = Sound(Audio(resource_path("assets/msgIco/music-box.mp3"), volume=10))
        self.s.play()

    def _get_system_theme(self):
        system = platform.system()
        if system == "Windows":
            try:
                import winreg
                registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                return "Light" if value == 1 else "Dark"
            except Exception:
                return "Unknown"
        elif system == "Darwin":
            try:
                result = subprocess.run(
                    ["defaults", "read", "-g", "AppleInterfaceStyle"],
                    capture_output=True, text=True
                )
                return "Dark" if "Dark" in result.stdout else "Light"
            except Exception:
                return "Light"
        elif system == "Linux":
            try:
                result = subprocess.run(
                    ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
                    capture_output=True, text=True
                )
                output = result.stdout.strip().lower()
                if "dark" in output:
                    return "Dark"
                elif "light" in output:
                    return "Light"
            except Exception:
                pass
            try:
                result = subprocess.run(
                    ["gsettings", "get", "org.cinnamon.desktop.interface", "gtk-theme"],
                    capture_output=True, text=True
                )
                theme = result.stdout.strip().strip("'").lower()
                if "dark" in theme:
                    return "Dark"
                else:
                    return "Light"
            except Exception:
                pass
            return "Unknown"
        else:
            return "Unknown"

    def showerror(self):
        self.show(type=0)

    def showwarning(self):
        self.show(type=1)

    def showinfo(self):
        self.show(type=2)

    def askquestion(self):
        return self.show(type=3) 

    def showask(self):
        self.show(type=4)

    def showscreenshot(self):
        self.show(type=5)

    def show(self, type=0):
        theme = self._get_system_theme()
        import tkinter as tk
        from PIL import Image, ImageTk
        from tkinter import ttk

        root = tk.Tk()
        bg_color = "#f0f0f0" if theme == "Light" else "#2e2e2e"
        fg_color = "#000000" if theme == "Light" else "#ffffff"
        root.config(bg=bg_color)

        type_str = str(type).zfill(2)
        icon_type = int(type_str[0])
        button_type = int(type_str[1])

 
        icons = {
            0: ("Error", "src/gamepie/assets/msgIco/gperr.png"),
            1: ("Warning", "src/gamepie/assets/msgIco/gpwarn.png"),
            2: ("Info", "src/gamepie/assets/msgIco/gpmsg.png"),
            3: ("Question", "src/gamepie/assets/msgIco/gpqest.png"),
            4: ("Information", "src/gamepie/assets/msgIco/gpinfo.png"),
            5: ("Screenshot", "src/gamepie/assets/msgIco/gpscrshot.png"),
        }
        title, icon_path = icons.get(icon_type, icons[0])
        if self._title:
            root.title(self._title)
        else:
            root.title(title)

        try:
            img = Image.open(icon_path)
        except Exception:
            img = Image.new("RGBA", (100, 100), (255, 0, 0, 255))
        img = img.resize((100, 100))
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(
            root,
            image=photo,
            text=self._msg,
            compound="left",
            font=("Arial", 12),
            anchor="nw",
            justify="left",
            bg=bg_color,
            fg=fg_color
        )
        label.pack(padx=10, pady=2, fill="both")

        def set_result(value):
            self.result = value
            root.destroy()

  
        button_map = {
            0: [],  # žádná tlačítka
            1: [("OK", lambda: set_result("ok"))],
            2: [("OK", lambda: set_result("ok")), ("Cancel", lambda: set_result("cancel"))],
            3: [("Yes", lambda: set_result("yes")), ("No", lambda: set_result("no")), ("Cancel", lambda: set_result("cancel"))],
            4: [("OK", lambda: set_result("ok"))], 
            5: [("Close", lambda: set_result("close"))],
            67:[("67", lambda: set_result("six seven"),),("41", lambda: set_result("four one"))],
        }

        if button_type in button_map and button_map[button_type]:
            button_frame = tk.Frame(root, bg=bg_color)
            button_frame.pack(pady=10)
            for text, cmd in button_map[button_type]:
                style = ttk.Style()
                style.configure("Custom.TButton", padding=0, font=("Arial", 11))
                btn = ttk.Button(button_frame, text=text, command=cmd, style="Custom.TButton")
                btn.pack(side="left", padx=5)

        root.resizable(False, False)
        root.after(30000, lambda: root.destroy())
        root.mainloop()
        return self.result
