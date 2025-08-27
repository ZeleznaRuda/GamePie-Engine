import random
import gamepie
from gamepie.plugins import Controllers

screen = gamepie.Window(title="Adventure Platformer", flags=gamepie.utils.RESIZABLE)
gamecamera = gamepie.Camera(position=(0, 0), zoom=1, anchor="center")

# hráč
player_run = gamepie.Frames(r"platformplug.jumper_go")
player_jump = gamepie.Frames(r"platformplug.jumper_jump")
player_stand = gamepie.Frames(r"platformplug.jumper_stand")
jump_sound = gamepie.mixer.Sound(gamepie.load.Audio("sound.effect.jump"))
player = gamepie.draw.Animation(
    screen, position=(1000, -1000), frames=player_run, ms=300,
    size=(45*2, 30*3), camera=gamecamera, anchor=gamepie.utils.CENTER
)


def generate_adventure_world():

    TILE_WIDTH = 120
    TILE_HEIGHT = 680
    WORLD_LENGTH = 255
    blocks = []
    current_y = 0
    for i in range(WORLD_LENGTH):
        current_y += random.randint(-2, 2) * 30
        if current_y < -400: current_y = -400
        if current_y > 0: current_y = 0
        blocks.append(gamepie.draw.Rectangle(
            screen,
            position=(i*TILE_WIDTH, current_y),
            size=(TILE_WIDTH, TILE_HEIGHT),
            color=(0,80,0),
            camera=gamecamera,
            anchor=gamepie.utils.CENTER
        ))
        blocks.append(gamepie.draw.Rectangle(
            screen,
            position=(i*TILE_WIDTH, current_y+250),
            size=(TILE_WIDTH, TILE_HEIGHT),
            color=(0,20,0),
            camera=gamecamera,
            anchor=gamepie.utils.CENTER
        ))
    return gamepie.utils.Objects(*blocks)


map = generate_adventure_world()

map = generate_adventure_world()
map_blocks = list(map.all())  # převod generatoru na seznam



controller = Controllers.PlatformController(player=player, camera=gamecamera,camera_offset=(-100,-100), gravity=0.8, speed=0.2, jump_power=13, objects=map(),movement_3_key=("left","right","up"))

def update():
    dt = screen.fps.tick()
    controller.update(dt)

    # smrt na trny
    for block in map.all():
        if block.color == (255,0,0) and block.collision.rect(player):
            player.pos = (100, -200) # reset
    if controller.status == "right":
        player.flip = (False,False)
        player.animation = player_run
        player.play()
    elif controller.status == "left":
        player.flip = (True,False)
        player.animation = player_run
        player.play()
    elif controller.status == "jump":
        if gamepie.wait(1000,f"PlayerJumpSound.{id(map()[6])}:S"):jump_sound.play()
        player.animation = player_jump
        player.play()
    elif controller.status == "falling":
        player.animation = player_jump
        player.play()
    else:
        player.animation = player_stand
        player.play()
    screen.fill(gamepie.utils.Color("SKY")())
    map.draw()
    player.draw()
    screen.flip()

screen.run()
gamepie.quit()
