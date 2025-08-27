import os
import shutil
import json
import tempfile
import subprocess
from gamepie.core import _gp_log
from urllib.parse import urlparse

protected_plugins = ["GUIassets","Controllers"]

# ai//t:my
def install(input_path):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    plugins_folder = os.path.join(current_folder, "")

    if not os.path.exists(plugins_folder):
        os.makedirs(plugins_folder)

    if input_path.startswith("http://") or input_path.startswith("https://"):
        parsed_url = urlparse(input_path)
        folder_name = os.path.basename(parsed_url.path).replace(".git", "")
        temp_dir = tempfile.mkdtemp()

        answer = input(f"Are you sure you want to download and install '{folder_name}' from {input_path}? This could be harmful (Y/n): ")
        if answer.lower() not in ["y", "yes", ""]:
            _gp_log("[plugin warning]: Installation canceled by user.")
            return

        try:
            subprocess.check_call(["git", "clone", input_path, os.path.join(temp_dir, folder_name)])
            input_path = os.path.join(temp_dir, folder_name)
        except Exception as e:
            _gp_log(f"[plugin warning]: Failed to clone repository: {e}")
            return
    else:
        folder_name = os.path.basename(input_path)

    has_gpplug = any(
        f.endswith(".gpplugin") and os.path.isfile(os.path.join(input_path, f))
        for f in os.listdir(input_path)
    )

    if has_gpplug:
        destination = os.path.join(plugins_folder, folder_name)

        if os.path.exists(destination):
            shutil.rmtree(destination)

        shutil.copytree(input_path, destination)
        _gp_log(f"[plugin info]: Plugin '{folder_name}' has been installed in 'plugins/'.")
    else:
        _gp_log("[plugin warning]: This folder is not a Gamepie plugin "
                "(to make it a plugin, create a .gpplugin file in the first level of the folder).")

def uninstall(name):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    plugins_folder = os.path.join(current_folder, "")
    target_folder = os.path.join(plugins_folder, name)

    if not os.path.isdir(target_folder):
        _gp_log(f"[plugin warning]: Plugin folder '{name}' was not found in 'plugins/'.")
        return

    gpplug_files = [
        f for f in os.listdir(target_folder)
        if f.endswith(".gpplugin") and os.path.isfile(os.path.join(target_folder, f))
    ]

    if gpplug_files:
        if name in protected_plugins:
            _gp_log(f"[plugin warning]: Plugin folder '{name}' is protected and cannot be removed.")
            return

    shutil.rmtree(target_folder)
    _gp_log(f"[plugin info]: Plugin folder '{name}' has been removed from 'plugins'")
