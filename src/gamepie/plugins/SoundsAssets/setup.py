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

_gp_register('sound.music.game_loop', r"plugins/SoundsAssets/pixabay/game-music-loop-6-144641.mp3")
_gp_register('sound.sword.fantasy_swing', r"plugins/SoundsAssets/pixabay/fantasy-game-sword-cut-sound-effect-get-more-on-my-patreon-339824.mp3")
_gp_register('sound.sword.rpg_attack_1', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-22-388940.mp3")
_gp_register('sound.sword.rpg_attack_2', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-23-388944.mp3")
_gp_register('sound.sword.rpg_attack_3', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-24-388941.mp3")
_gp_register('sound.sword.rpg_attack_4', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-29-388954.mp3")
_gp_register('sound.sword.rpg_attack_5', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-30-388949.mp3")
_gp_register('sound.sword.rpg_attack_6', r"plugins/SoundsAssets/pixabay/rpg-sword-attack-combo-34-388950.mp3")
_gp_register('sound.sword.hit', r"plugins/SoundsAssets/pixabay/sword-hit-7160.mp3")
_gp_register('sound.sword.metal', r"plugins/SoundsAssets/pixabay/metal-sound-fighting-game-87507.mp3")
_gp_register('sound.effect.collect', r"plugins/SoundsAssets/pixabay/collect-points-190037.mp3")
_gp_register('sound.effect.damage', r"plugins/SoundsAssets/pixabay/damage-40114.mp3")
_gp_register('sound.effect.falling', r"plugins/SoundsAssets/pixabay/falling-game-character-352287.mp3")
_gp_register('sound.effect.bonus', r"plugins/SoundsAssets/pixabay/game-bonus-02-294436.mp3")
_gp_register('sound.effect.bonus2', r"plugins/SoundsAssets/pixabay/game-bonus-144751.mp3")
_gp_register('sound.effect.explosion', r"plugins/SoundsAssets/pixabay/game-explosion-321700.mp3")
_gp_register('sound.effect.pop', r"plugins/SoundsAssets/pixabay/pop-sound-effect-197846.mp3")
_gp_register('sound.effect.jump', r"plugins/SoundsAssets/pixabay/retro-jump-3-236683.mp3")
_gp_register('sound.effect.laser', r"plugins/SoundsAssets/pixabay/laser-312360.mp3")
_gp_register('sound.effect.pingpong', r"plugins/SoundsAssets/pixabay/ping-pong-ball.mp3")
_gp_register('sound.system.start', r"plugins/SoundsAssets/pixabay/game-start-317318.mp3")
_gp_register('sound.system.start2', r"plugins/SoundsAssets/pixabay/game-start-6104.mp3")
_gp_register('sound.system.start3', r"plugins/SoundsAssets/pixabay/gamestart-272829.mp3")
_gp_register('sound.system.countdown', r"plugins/SoundsAssets/pixabay/game-countdown-62-199828.mp3")
_gp_register('sound.system.winner', r"plugins/SoundsAssets/pixabay/winner-bell-game-show-91932.mp3")
_gp_register('sound.ambient.birds', r"plugins/SoundsAssets/pixabay/bird-song-bright-distant-forest-life-chirps-tonal-light-air-02-386311.mp3")
_gp_register('sound.ambient.horror', r"plugins/SoundsAssets/pixabay/horror-game-ambiance-292952.mp3")
_gp_register('sound.other.nyan', r"plugins/SoundsAssets/pixabay/nyan.mp3")
_gp_register('sound.other.nomnom', r"plugins/SoundsAssets/pixabay/nom_nom.mp3")

