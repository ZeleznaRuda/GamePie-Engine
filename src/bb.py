import gamepie

# okno a kamera
screen = gamepie.Window(title="BB", flags=gamepie.utils.RESIZABLE)
gamecamera = gamepie.Camera(position=(0, 0), zoom=1, anchor="topleft")

# textura bloku
brick_texture = gamepie.load.Texture("brick")

# seznam bloků
blocks = []

# velikost jedné buňky v mřížce
TILE_SIZE = 40

def snap_to_grid(pos):
    x, y = pos
    grid_x = (x // TILE_SIZE) * TILE_SIZE
    grid_y = (y // TILE_SIZE) * TILE_SIZE
    return grid_x, grid_y

def update():
    dt = screen.fps.tick()
    screen.fill(gamepie.utils.Color("SKY")())

    if gamepie.mouse.left:
        mouse_pos = gamepie.mouse.pos
        grid_pos = snap_to_grid(mouse_pos)
        exists = any(block.pos == grid_pos for block in blocks)
        if not exists:
            block = gamepie.draw.Image(
                screen,
                brick_texture,
                position=grid_pos,
                size=(TILE_SIZE, TILE_SIZE),
                camera=gamecamera,
                anchor=gamepie.utils.TOPLEFT
            )
            blocks.append(block)
    for block in blocks:
        block.draw()

    screen.flip()

screen.run()
