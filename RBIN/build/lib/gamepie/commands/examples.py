import os
import argparse
from datetime import date

def main():
    parser = argparse.ArgumentParser(
        description="Generate example GamePie code templates."
    )
    parser.add_argument(
        "code_choice",
        choices=["1", "2"],
        help="Template number (1 or 2)."
    )
    parser.add_argument(
        "output_folder",
        help="Destination folder to save the generated file."
    )

    args = parser.parse_args()

    templates = {
        "1": '''
import gamepie # << import library

screen = gamepie.Window(title="Test", flags=gamepie.RESIZABLE) # << create window
fps = gamepie.Clock(60)                                       # << create clock

pie_texture = gamepie.load.Texture("pie")            # << load assets
pie = gamepie.draw.Image(screen, texture=pie_texture) # << create game object

def update():         # << main loop (mandatory!)
    dt = fps.tick()   # << delta time calculation
    speed = 0.1 * dt  # << smooth movement using delta time
    
    pie.x += speed    # << game logic
    
    screen.fill(gamepie.WHITE) # << clear the screen
    pie.draw()                 # << draw object
    screen.flip()              # << update the screen
    
screen.run()   # << start application (mandatory!)
gamepie.quit() # << exit
''',
        "2": '''
import gamepie # << import library

screen = gamepie.Window(title="Test", flags=gamepie.NOFRAME) # << create borderless window
fps = gamepie.Clock(60)                                      # << create clock

nyan = gamepie.load.Animation("nyancat", ms=60) # << load animation
gamepie.mixer.Music("nyansound")                # << load and play music
anim = gamepie.draw.Animation(screen, animation=nyan, size=(800, 600), camera=gamepie.uicamera) # << create animation

anim.play() # << start animation

def update():           # << main loop (mandatory!)
    screen.fill((0, 0, 0)) # << clear screen (black)
    dt = fps.tick()        # << delta time calculation
    anim.draw()            # << draw animation
    screen.flip()          # << update the screen

screen.run()   # << start application (mandatory!)
gamepie.quit() # << exit
'''
    }

    code = templates.get(args.code_choice)
    if code is None:
        parser.error(f"Unknown template choice: {args.code_choice}")

    today = date.today()
    date_str = today.isoformat()

    filename = f"template-{date_str}.py"
    filepath = os.path.join(args.output_folder, filename)

    try:
        os.makedirs(args.output_folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"File saved to: {filepath}")
    except Exception as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    main()
