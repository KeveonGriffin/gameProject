import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

def screen_coords(x,y):
    return(x * GRID_SIZE, y * GRID_SIZE)
def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_HEIGHT):
            screen.blit("floor2", screen_coords(x,y))
def draw():
    draw_background()
pgzrun.go()