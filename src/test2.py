import gamepie
from gamepie import plugins
screen = gamepie.Window(title="Test",flags=gamepie.utils.RESIZABLE)
music = gamepie.mixer.Music(gamepie.load.Audio("music"))
btnP = gamepie.plugins.GUIassets.Button(screen,text="",image=gamepie.load.Texture("play_audio"),size=(90,50),position=(0,0),camera=gamepie.utils.uicamera)
btnM = gamepie.plugins.GUIassets.Button(screen,text="",image=gamepie.load.Texture("mute_audio"),size=(90,50),position=(90,0),camera=gamepie.utils.uicamera)

def update():
    dt = screen.fps.tick()
    screen.fill((255,255,255))
    
    btnP.draw()
    btnM.draw()
    if btnP.is_press():
        
        music.unpause()
    elif btnM.is_press():
        music.pause()
    screen.flip()
screen.run()
