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
    global game_over, player, keys_to_collect, guards
    game_over = False
    player = Actor("player", anchor=("left", "top"))
    keys_to_collect = []
    guards = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = screen_coords(x, y)
            elif square == 'K':
                key = Actor("key", anchor=("left", "top"), \
                    pos = screen_coords(x,y))
                keys_to_collect.append(key)
            elif square == 'G':
                guard = Actor("guard", anchor=("left", "top"), \
                              pos=screen_coords(x,y))
                guards.append(guard)
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
    for key in keys_to_collect:
        key.draw()
    for guard in guards:
        guard.draw()
def draw_game_over():
    screen_middle = (WIDTH / 2, HEIGHT / 2)
    screen.draw.text("...Game Over...", midbottom= screen_middle, \
                     fontsize=GRID_SIZE, color="red",owidth=1)
def draw():
    draw_background()
    draw_scenery
    draw_actors()
    if game_over:
        draw_game_over()
def on_key_down(key):
    if key == keys.LEFT:
        move_player(-1, 0)
    elif key == keys.UP:
        move_player(0, -1)
    elif key == keys.RIGHT:
        move_player(1,0)
    elif key == keys.DOWN:
        move_player(0, 1)
def move_player(dx, dy):
    global game_over
    if game_over:
        return
    (x, y) = grid_coords(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == 'W':
        return
    elif square == 'D':
        if len(keys_to_collect) > 0:
            return
        else:
            game_over = True
    for key in keys_to_collect:
        (key_x, key_y) = grid_coords(key)
        if x == key_x and y == key_y:
            keys_to_collect.remove(key)
            break
    player.pos = screen_coords(x, y)
def move_guard(guard):
    global game_over
    if game_over:
        return
    (player_x, player_y) = grid_coords(player)
    (guard_x, guard_y) = grid_coords(guard)
    if player_x > guard_x and MAP[guard_x + 1][guard_y] != "W":
        guard_x += 1
    elif player_x < guard_x and MAP[guard_x - 1][guard_y] != "W":
        guard_x -= 1
    elif player_y > guard_y and MAP[guard_x][guard_y + 1] != "W":
        guard_y += 1
    elif player_y > guard_y and MAP[guard_x][guard_y - 1] != "W":
        guard_y -= 1
    guard.pos = screen_coords(guard_x, guard_y)
    if guard_x == player_x and guard_y == player_y:
        game_over = True
setup_game()
pgzrun.go()


