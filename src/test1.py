import gamepie 

screen = gamepie.Window(title="Test", flags=gamepie.utils.RESIZABLE)                          

e = gamepie.draw.Ellipse(screen, position=(0, 0), size=(200, 100), color=(255, 0, 0), anchor=gamepie.utils.CENTER).outline((0, 0, 0), 5)

def update():         
    screen.fill((255, 255, 255))
    dt = screen.fps.tick()
    gamepie.draw.polygon(
        surface=screen,                      # The target surface (e.g., your game window)
        color=(0, 255, 0),                   # Polygon color (green)
        points=[(0, 0), (800, 0), (400, 300)],  # List of (x, y) vertices
        width=5,                             # 0 for filled polygon, >0 for outline
        angle=0,                             # Rotation angle in degrees
        flip=(False, False)                  # Flip horizontally/vertically
    )
    e.draw()
    screen.flip()

screen.run()   
gamepie.quit() 