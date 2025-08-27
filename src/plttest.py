import gamepie

screen = gamepie.Window(title="Parkour master", flags=gamepie.utils.RESIZABLE)



count = gamepie.draw.gui.Label(screen,position=(0, 0), font=gamepie.load.Font(size=20),text="Time: null",anti_aliasing=True,background_color=None,visible=True)


gamecamera = gamepie.Camera(position=(0, 0), zoom=1, anchor="center")


player_texture = gamepie.Texture("platformplug.jumper")
spike_textures = gamepie.Texture("platformplug.spike")

end_flag_textures = gamepie.Texture("platformplug.end_flag")


player_run = gamepie.Frames(r"platformplug.jumper_go")
player_jump = gamepie.Frames(r"platformplug.jumper_jump")
player_stand = gamepie.Frames(r"platformplug.jumper_stand")
death_sound = gamepie.mixer.Sound(gamepie.Audio("platformplug.jumper_death_sound",volume=50))
jump_sound = gamepie.mixer.Sound(gamepie.load.Audio("sound.effect.jump"))

player = gamepie.draw.Animation(screen,position=(400 ,-480), frames=player_run,ms=300, size=(45 * 2, 30 * 3), camera=gamecamera,anchor=gamepie.utils.CENTER)

youwin_label = gamepie.draw.gui.Label(screen,position=(2480, -480), font=gamepie.load.Font("DejaVu Sans",50),text="Vyhrál jsi :)",background_color=None,anti_aliasing=True ,camera=gamecamera,anchor=gamepie.utils.TOPLEFT,visible=True)


spikes = gamepie.utils.Objects(
    gamepie.draw.Image(screen, texture=spike_textures, position=(380, -73), size=(64, 64), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Image(screen, texture=spike_textures, position=(1850, -380), size=(64, 64), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Image(screen, texture=spike_textures, position=(2250, -380), size=(64, 64), camera=gamecamera, anchor=gamepie.utils.CENTER),

)

map = gamepie.utils.Objects(
    gamepie.draw.Rectangle(screen, position=(-380, 100), size=(200, 30), color=(200, 200, 200), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(-50, 80), size=(120, 25), color=(128,128,128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(130, 40), size=(120, 25), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(380, -40), size=(250, 25), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(650, -100), size=(120, 25), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(880, -140), size=(140, 25), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1100, -180), size=(120, 30), color=(116, 116, 116), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1290, -270), size=(120, 30), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1480, -335), size=(120, 30), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1480, -335), size=(260, 30), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1480, -335), size=(260, 30), color=(220, 180, 180), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(1680, -335), size=(120, 30), color=(128, 128, 128), camera=gamecamera, anchor=gamepie.utils.CENTER),
    gamepie.draw.Rectangle(screen, position=(2580, -335), size=(260, 30), color=(220, 180, 180), camera=gamecamera, anchor=gamepie.utils.CENTER),
)
end_block = gamepie.draw.Image(screen,texture=end_flag_textures ,position=(2450, -335), size=(128, 256), camera=gamecamera, anchor=gamepie.utils.BOTTOMLEFT)

nmsp = gamepie.utils.Namespace({
    "platformBack": False,
    "time": 0,
})



controller = gamepie.plugins.Controllers.PlatformController(player=player,camera=gamecamera,speed=0.2,jump_power=13, objects=map(),movement_3_key=("left","right","up"))

tck = 0

def update():
    global tck
    dt = screen.fps.tick()
    tck += 1
    
    controller.update(dt)
    for spike in spikes.all():
        if spike.collision.rect(player,offset=(32, 0,-48, 0)) or player.y >= 500:
            player.color = (255,0,0)
            player.pos =(-400, 100)
            nmsp.set("time", 0)
            death_sound.play()
    if controller.status == "right":
        player.flip = (False,False)
        player.animation = player_run
        player.play()
    elif controller.status == "left":
        player.flip = (True,False)
        player.animation = player_run
        player.play()
    elif controller.status == "jump":
        if gamepie.wait(500,f"PlayerJumpSound.{id(map()[6])}:S"):jump_sound.play()
        player.animation = player_jump
        player.play()
    elif controller.status == "falling":
        player.animation = player_jump
        player.play()
    else:
        player.animation = player_stand
        player.play()
        

    if gamepie.wait(500,f"SwitchBlock.{id(map()[6])}:<"):
        map()[6].enable = True
    elif gamepie.wait(1000,f"SwitchBlock.{id(map()[6])}:>"):
        map()[6].enable = False
    if not map()[12].collision.rect(player):
        nmsp.set("time", nmsp.get("time") + 1)
        
    if gamepie.wait(500,f"PlayerKillColor.{id(map()[6])}:Normal"):player.color = (255,255,255) 
    platform = map()[11]  
    if not nmsp()["platformBack"]: 
        platform.x += 3
        if platform.x >= 2580:
            nmsp.set("platformBack" ,True)
    else: 
        platform.x -= 3
        if platform.x <= 1680:
            nmsp.set("platformBack" ,False)
    screen.fill(gamepie.utils.Color("SKY")())
    count.text = f"Time: {nmsp().get('time')}"
    youwin_label.draw()
    player.draw()
    spikes.draw()
    map.draw()
    end_block.draw()
    count.draw()
    

    screen.flip()

screen.run()
gamepie.quit()
