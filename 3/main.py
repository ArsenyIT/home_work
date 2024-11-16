from tank import Tank
from tkinter import*
import world
import tanks_collection
import texture

KEY_UP = 38
KEY_DOWN = 40
KEY_LEFT = 37
KEY_RIGHT = 39

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

FPS = 60

def update():
    tanks_collection.update()
    player = tanks_collection.get_player()
    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2, player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)
    w.after(1000//FPS, update)

def key_press(event):
    player = tanks_collection.get_player()
    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(delta_x = 0, delta_y = -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(delta_x = 0, delta_y = 5)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(delta_x = 5, delta_y = 0)
    elif event.keycode == KEY_LEFT:
        world.move_camera(delta_x = -5, delta_y = 0)

    elif event.keycode == 32:
        tanks_collection.spawn_enemy()

def load_textures():
    texture.load('file_up', '../img/Tank Up.png')
    texture.load('file_down', '../img/Tank Down.png')
    texture.load('file_left', '../img/Tank Left.png')
    texture.load('file_right', '../img/Tank Right.png')
    print(texture._frames)

w = Tk()

load_textures()

w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT, bg="alice blue")
canv.pack()

tanks_collection.initialze(canv)

w.bind('<KeyPress>', key_press)

update()
w.mainloop()