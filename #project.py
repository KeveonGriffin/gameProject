import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
MAP = ["WWWWWWWWWWWWWWWW",
       "w              w",
       "W              w",
       "w   w   KG     W",
       "W   WWWWWWWWW  W",
       "w              w",
       "w        P     w",
       "W   WWWWWWWWW  W",
       "w        GK  W w",
       "w              w",
       "w              D",
       "WWWWWWWWWWWWWWWW"]

def screen_coords(x,y):
    return(x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", screen_coords(x,y))
def draw_scenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", screen_coords(x, y))
            elif square == "D":
                screen.blit("door", screen_coords(x,y))
def draw():
    draw_background()
    draw_scenery

pgzrun.go()
