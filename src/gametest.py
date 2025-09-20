import gamepie
#create window
screen = gamepie.Window(title="Test",flags=gamepie.constants.RESIZABLE)
#fps
fps = gamepie.Clock(60)
gamepie.mixer.Music(gamepie.load.Audio("gp:gp.sound.music"))
#loads
font = gamepie.load.Font("DejaVuSans",size=50)
img = gamepie.load.Texture("pie")
player_img = gamepie.load.Texture("brick")

nom = gamepie.mixer.Sound(gamepie.load.Audio("sound.effect.collect"))
#shape
pie = gamepie.draw.rect(screen,position=(50,50),anchor=gamepie.constants.CENTER,camera=gamepie.utils.uicamera).outline((0,0,0),3)
player = gamepie.draw.Image(screen,texture=player_img,anchor=gamepie.constants.CENTER, position=(0,0), size=(70, 70), camera=gamepie.utils.uicamera).outline((0,0,0),2)

#label
text = gamepie.draw.gui. Label(screen,text=".",color=(0,255,0),font=font,anti_aliasing=True,background_color=None)

score = 0
speed = 1
#loop
def update():
    global speed, score
    dt = fps.tick()
    pie = gamepie.draw.blur_rect(pie,50)
    
    if gamepie.key.is_down("w"):
        player.y -= speed* dt
        player.angle = 90
    if gamepie.key.is_down("s"):
        player.y += speed* dt
        player.angle = -90
        player.flip = ((False,True))
    if gamepie.key.is_down("a"):
        player.x -= speed* dt
        player.angle = -180
        player.flip = ((False,True))
    if gamepie.key.is_down("d"):
        player.x += speed* dt
        player.angle = 0
        player.flip = ((False,False))

    if player.collision.rect(pie): 
        nom.play()
        speed = 0.5

        score += 1

    if gamepie.wait(5000, "0"):
        speed = 0.2
        

    
    text.text = f"Score: {score}"
    screen.fill((0,80,25))
    pie.draw()
    player.draw()
    text.draw()
    screen.flip()
    
#running
screen.run()
gamepie.quit()
