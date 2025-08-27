import gamepie


screen = gamepie.Window(title="Test")

fps = gamepie.Clock(60)
font = gamepie.loadfn.Font("arial",size=20)
text = gamepie.gobjects.Text(surface=screen,color=(0,255,0),font=font,anti_aliasing=True,text="").outline((0,0,0),2)

def update(): 
    dt = fps.tick()
    screen.fill((0,80,25))

    text.text = f"Don't shout;Volume: {gamepie.input.microphone.volume}"
    if gamepie.input.microphone.volume >= 2:
        gamepie.quit()
    text.pos = gamepie.input.mouse.pos
    text.draw()


    screen.flip()

screen.run()
gamepie.quit()