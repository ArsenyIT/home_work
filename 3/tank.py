from hitbox import Hitbox
from tkinter import PhotoImage, NW

class Tank:

    __count = 0
    __SIZE = 100

    def __init__(self, canvas, x, y, model = 'Т-14 Армата', ammo = 100, speed = 10, file_up = '../img/Tank Up.png', file_down = '../img/Tank Down.png', file_right = '../img/Tank Right.png', file_left = '../img/Tank Left.png'):
        self.__skin_up = PhotoImage(file=file_up)
        self.__skin_down = PhotoImage(file=file_down)
        self.__skin_right = PhotoImage(file=file_right)
        self.__skin_left = PhotoImage(file=file_left)
        self.__hitbox = Hitbox(x, y, Tank.__SIZE, Tank.__SIZE)
        Tank.__count += 1
        self.__canvas = canvas
        self.__fuel = 100
        self.__speed = speed
        self.__model = model
        self.__xp = 0
        self.__hp = 100
        self.__ammo = ammo
        self.__x = x
        self.__y = y
        if self.__x < 0:
            self.__x = 0
        if self.__y < 0:
            self.__y = 0

        self.__create()

    def fire(self):
        if self.__ammo > 0:
            self.__ammo -= 1
            print('Стреляю')

    def info(self):
        print(f'Модель: {self.__model}, Опыт: {self.__xp}, Здоровье: {self.__hp},'
        f' Патроны: {self.__ammo}, Топливо: {self.__fuel}, Координаты: {self.__x},{self.__y}')

    def forvard(self):
        if self.__fuel > 0:
            self.__y += -self.__speed
            self.__fuel -= 1
            self.__canvas.itemconfig(self.__id, image=self.__skin_up)
            self.__repaint()
            self.__update_hitbox()
            print('Ход вверх')

    def backward(self):
        if self.__fuel > 0:
            self.__y += self.__speed
            self.__fuel -= 1
            self.__canvas.itemconfig(self.__id, image=self.__skin_down)
            self.__repaint()
            self.__update_hitbox()
            print('Ход вниз')

    def left(self):
        if self.__fuel > 0:
            self.__x += -self.__speed
            self.__fuel -= 1
            self.__canvas.itemconfig(self.__id, image=self.__skin_left)
            self.__repaint()
            self.__update_hitbox()
            print('Ход влево')

    def right(self):
        if self.__fuel > 0:
            self.__x += self.__speed
            self.__fuel -= 1
            self.__canvas.itemconfig(self.__id, image=self.__skin_right)
            self.__repaint()
            self.__update_hitbox()
            print("Ход вправо")

    def __create(self):
        self.__id = self.__canvas.create_image(self.__x, self.__y, image=self.__skin_up, anchor=NW)

    def __repaint(self):
        self.__canvas.moveto(self.__id, x = self.__x, y = self.__y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.__x, self.__y)

    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_ammo(self):
        return self.__ammo

    def get_fuel(self):
        return self.__fuel

    def get_xp(self):
        return self.__xp

    def get_hp(self):
        return self.__hp

    def get_model(self):
        return self.__model

    def get_speed(self):
        return self.__speed

    @staticmethod
    def get_count(self):
        return Tank.__count

    @staticmethod
    def get_size(self):
        return Tank.__SIZE

    def __str__(self):
        return(f'Координаты: х = {self.__x}, y = {self.__y}, Модель: model = {self.__model}, Здоровье: hp = {self.__hp}, Боеприпасы: ammo = {self.__ammo}, Опыт: хp = {self.__xp}, Боеприпасы: ammo = {self.__ammo}, Опыт: хp = {self.__xp},')
