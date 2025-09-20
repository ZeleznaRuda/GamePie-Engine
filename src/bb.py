
import gamepie


screen = gamepie.Window(title="BB",print_fps=True,maximize=True)
screen.escape = False
gamecamera = gamepie.Camera(position=(0,0), zoom=1, anchor="center")


blocks = []

GPSAVE_FILE = "world.json"

TILE_SIZE = 40
WORLD_WIDTH = 800
WORLD_HEIGHT = 21

STONE_LAYER = 15
DIRT_LAYER = 5
GRASS_LAYER = 1

def snap_to_grid(pos):
    world_x = pos[0] - screen.w // 2 + gamecamera.x
    world_y = pos[1] - screen.h // 2 + gamecamera.y
    grid_x = (world_x // TILE_SIZE) * TILE_SIZE
    grid_y = (world_y // TILE_SIZE) * TILE_SIZE
    return grid_x, grid_y


blocks_types = gamepie.utils.Namespace({
    "Oak planks": gamepie.load.Texture("gp:brick_building.textures.oak_planks"),
    "Stone brick": gamepie.load.Texture("gp:brick_building.textures.stone_brick"),
    "Grass": gamepie.load.Texture("gp:brick_building.textures.grass"),
    "Dirt": gamepie.load.Texture("gp:brick_building.textures.dirt"),
    "Brick": gamepie.load.Texture("gp:brick_building.textures.brick"),
    "Oak": gamepie.load.Texture("gp:brick_building.textures.oak"),
    "Stone": gamepie.load.Texture("gp:brick_building.textures.stone"),
    "Leaves": gamepie.load.Texture("gp:brick_building.textures.leaves"),
    "Glass": gamepie.load.Texture("gp:brick_building.textures.glass"),
    "Stone stairs": gamepie.load.Texture("gp:brick_building.textures.stone_stairs"),
    "Door": gamepie.load.Texture("gp:brick_building.textures.door")
})
block_c_index = 1
type_of_block_gui_text = gamepie.draw.gui.Label(screen, font=gamepie.load.Font(),position=(10,5),background_color=None)
show_type_c_block_gui = gamepie.draw.Image(
                screen,
                blocks_types.getaslist(int(block_c_index))[0],
                position=(10,25),
                size=(40, 40),
                camera=gamepie.utils.uicamera,
                anchor=gamepie.constants.TOPLEFT
            ).outline((0,0,0),2)


def save_world(filename=GPSAVE_FILE):
    import json
    data = []
    for block in blocks:
        block_type = None
        for k, v in blocks_types._dict.items():
            if v == block.texture:
                block_type = k
                break
        data.append({
            "pos": block.pos,
            "flip": block.flip,
            "size": block.size,
            "type": block_type
        })
    gamepie.utils.gpdata_save(data, filename=filename)


def load_world(filename=GPSAVE_FILE):
    global blocks
    blocks = []
    data = gamepie.utils.gpdata_load(filename)
    for b in data:
        tex = blocks_types.get(b.get("type"))
        if tex:
            block = gamepie.draw.Image(
                screen,
                tex,
                position=tuple(b.get("pos")),
                flip=tuple(b.get("flip")),
                size=tuple(b.get("size", (TILE_SIZE, TILE_SIZE))),
                camera=gamecamera,
                anchor=gamepie.constants.TOPLEFT,
            )
            blocks.append(block)

def generate_world():
    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            grid_x = x * TILE_SIZE
            grid_y = y * TILE_SIZE

            if y >= WORLD_HEIGHT - STONE_LAYER:
                tex = blocks_types.get("Stone")
            elif y >= WORLD_HEIGHT - (STONE_LAYER + DIRT_LAYER):
                tex = blocks_types.get("Dirt")
            elif y >= WORLD_HEIGHT - (STONE_LAYER + DIRT_LAYER + GRASS_LAYER):
                tex = blocks_types.get("Grass")
            else:
                continue

            block = gamepie.draw.Image(
                screen,
                tex,
                position=(grid_x, grid_y),
                size=(TILE_SIZE, TILE_SIZE),
                camera=gamecamera,
                anchor=gamepie.constants.TOPLEFT
            )
            blocks.append(block)


load_world()

def has_block_at(pos):
    return any(b.pos == pos for b in blocks)

def update():
    global block_c_index


    screen.fill(gamepie.utils.Color("SKY")())

    if gamepie.key.char and gamepie.key.char.isdigit() :
        block_c_index = gamepie.key.char

    max_index = len(blocks_types()) - 1
    wheel_value = gamepie.mouse.int_mousewheel
    if 0 <= wheel_value <= max_index:
        block_c_index = wheel_value


    show_type_c_block_gui.texture = blocks_types.getaslist(int(block_c_index))[0]
    mouse_pos = gamepie.mouse.pos
    grid_pos = snap_to_grid(mouse_pos)

    type_of_block_gui_text.text = blocks_types.getaslist(int(block_c_index))[1]

    if gamepie.mouse.left:
        if not has_block_at(grid_pos):
            tex = blocks_types.getaslist(int(block_c_index))[0]
            size = (TILE_SIZE, TILE_SIZE)
            if blocks_types.getaslist(int(block_c_index))[1] == "Door":
                size = (TILE_SIZE, TILE_SIZE * 2)
            block = gamepie.draw.Image(
                screen,
                tex,
                position=grid_pos,
                size=size,
                camera=gamecamera,
                anchor=gamepie.constants.TOPLEFT
            )
            blocks.append(block)

    if gamepie.mouse.right:
        for block in blocks:
            if block.pos == grid_pos:
                blocks.remove(block)
                break



    if gamepie.key.is_down("r") and gamepie.wait(500, "--*"):
        for b in blocks:
            if b.pos == grid_pos:
                b.flip = (not b.flip[0], b.flip[1])
                break

    if gamepie.key.is_down("right"): gamecamera.x += TILE_SIZE //2
    if gamepie.key.is_down("left"): gamecamera.x -= TILE_SIZE //2
    if gamepie.key.is_down("down"): gamecamera.y += TILE_SIZE //2
    if gamepie.key.is_down("up"): gamecamera.y -= TILE_SIZE  //2
    
    if gamepie.key.is_down("ctrl") and gamepie.key.is_down("home"):
        gamecamera.pos = (0, -600)
        blocks.clear()
        generate_world()
            
    if gamepie.key.is_down("home")and gamepie.wait(500, "--*"):
        gamecamera.pos = (0, -600)    
    if gamepie.key.is_down("escape")and gamepie.wait(500, "--*"):
        msgboxcwsc = gamepie.utils.Messagebox("Do you want to save your changes?").show(43)
        if msgboxcwsc == "yes":
            save_world()
            gamepie.quit()
        elif msgboxcwsc == "no":
            gamepie.quit()
        elif msgboxcwsc == "close":
            pass


    for block in blocks:
            block.draw()

    type_of_block_gui_text.draw()
    show_type_c_block_gui.draw()
    screen.flip()

screen.run()
save_world()
gamepie.quit()
