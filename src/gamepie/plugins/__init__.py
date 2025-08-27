import os, importlib

_plugin_dir = os.path.dirname(__file__)

for name in os.listdir(_plugin_dir):
    path = os.path.join(_plugin_dir, name)

    if os.path.isdir(path) and os.path.exists(os.path.join(path, "__init__.py")):
        full_name = f"{__package__}.{name}"
        module = importlib.import_module(full_name)
        globals()[name] = module

    elif name.endswith(".py") and name != "__init__.py":
        module_name = name[:-3]
        full_name = f"{__package__}.{module_name}"
        module = importlib.import_module(full_name)
        globals()[module_name] = module
