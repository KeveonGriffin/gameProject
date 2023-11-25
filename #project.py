import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W   W   KG     W",
       "W   WWWWWWWWW  W",
       "W              W",
       "W       P      W",
       "W   WWWWWWWWW  W",
       "W        GK  W W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]

def screen_coords(x,y):
    return(x * GRID_SIZE, y * GRID_SIZE)
def grid_coords(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
def setup_game():
    global player
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = screen_coords(x, y)
def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", screen_coords(x,y))
def draw_scenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[x][y]
            if square == "W":
                screen.blit("wall", screen_coords(x, y))
            elif square == "D":
                screen.blit("door", screen_coords(x,y))
def draw_actors():
    player.draw()
def draw():
    draw_background()
    draw_scenery
    draw_actors()
def on_key_down(key):
    if key == keys.LEFT:
        move_player(-1, 0)
    elif key == keys.UP:
        move_player(0, -1)
    elif key == keys.RIGHT:
        move_player(1,0)
    elif key == keys.DOWN:
        move_player(0, 1)
setup_game()
pgzrun.go()


