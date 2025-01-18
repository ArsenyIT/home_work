from random import randint
from units import Tank
import world

_tanks = []
_canvas = None

def initialze(canv):
    global _canvas
    _canvas = canv

    player = spawn(False)
    enemy = spawn(True).set_target(player)
    spawn(True).set_target(player)

    print(_tanks)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collishion(tank)

def check_collishion(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.intersect(other_tank):
            return True
    return False

    # def spawn_enemy():
    #     pos_x = randint(200, 800)
    #     pos_y = randint(200, 600)
    #
    #     t = Tank(_canvas, x=pos_x, y=pos_y, speed=1)
    #     if not check_collishion(t):
    #         t.set_target(get_player())
    #         _tanks.append(t)
    #         return True

def spawn(is_bot=True):
    cols = world.get_cols()
    rows = world.get_rows()

    while True:
        col = randint(1, cols - 1)
        row = randint(1, rows - 1)
        if world.get_block(row, col) != world.GROUND:
            continue

        t = Tank(_canvas, row, col, bot = is_bot)
        if not check_collishion(t):
            _tanks.append(t)
            return t