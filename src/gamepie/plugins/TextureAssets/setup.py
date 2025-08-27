from gamepie.pather import _gp_path_register_new as _gp_reg

__gp_registered_paths = {}

def _gp_register(name, path):
    __gp_registered_paths[name] = path
    _gp_reg(name, path)

def help():
    print("Sounds:")
    for name, path in __gp_registered_paths.items():
        print(f"{name}: {path}")


'''Thank you to the website 'pixabay' and its creators for allowing us to use their content.'''

_gp_register('texture.rpg.game_loop', r"plugins\SoundsAssets\pixabay\game-music-loop-6-144641.mp3")
_gp_register('texture.rpg.fantasy_swing', r"plugins\SoundsAssets\pixabay\fantasy-game-sword-cut-sound-effect-get-more-on-my-patreon-339824.mp3")
_gp_register('texture.platformer.brick', r"plugins\TextureAssets\libTextures\brick.png")
_gp_register('texture.system.mushroom', r"plugins\TextureAssets\libTextures\mushroom.png")
_gp_register('texture.system.pie', r"plugins\TextureAssets\libTextures\pie.png")
