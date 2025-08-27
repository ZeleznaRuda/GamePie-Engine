from gamepie.pather import _gp_path_register_new
from gamepie.load import Texture, loadfn
pie = loadfn.load(f"plugin/ass1/1.png",type=Texture)
_gp_path_register_new('piePlug',f"plugin/ass1/1.png")
