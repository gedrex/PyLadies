#!../venv/bin/python

import math
import pyglet
from pyglet import gl

WIDTH = 1400 
HEIGHT = 800
ROTATION_SPEED = 300
ACCELERATION = 30

pressed_keys = set()
#load image and give it anchors
def load_image(filename):
    image = pyglet.image.load(filename)
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    return image

spaceship_img = load_image('./spaceship.png')

#spaceship definition
class Spaceship:
    def __init__(self, window, rotation=0):
        self.window = window
        self.x = window.width / 2
        self.y = window.height / 2
        self.x_speed = 0
        self.y_speed = 0
        self.rotation = rotation
        self.sprite = pyglet.sprite.Sprite(spaceship_img, batch=batch) 

    def tick(self,dt):
        if pyglet.window.key.LEFT in pressed_keys:
            self.rotation += dt * ROTATION_SPEED

        if pyglet.window.key.RIGHT in pressed_keys:
            self.rotation -= dt * ROTATION_SPEED

        if pyglet.window.key.UP in pressed_keys:
            rotation_radians = math.radians(self.rotation)
            self.x_speed += dt * ACCELERATION * math.cos(rotation_radians)
            self.y_speed += dt * ACCELERATION * math.sin(rotation_radians)

        if pyglet.window.key.DOWN in pressed_keys:
            rotation_radians = math.radians(self.rotation)
            self.x_speed -= dt * ACCELERATION * math.cos(rotation_radians)
            self.y_speed -= dt * ACCELERATION * math.sin(rotation_radians)

        self.x += dt + self.x_speed
        self.y += dt + self.y_speed

        if self.x < 0:
            self.x += self.window.width
        if self.y < 0:
            self.y += self.window.height
        if self.x > self.window.width:
            self.x -= self.window.width
        if self.y > self.window.height:
            self.y -= self.window.height
        self.sprite.rotation = 90 - self.rotation
        self.sprite.x = self.x
        self.sprite.y = self.y
        

#objects what are going to be shown
objects = []

#events on objects
batch = pyglet.graphics.Batch()


def draw():
    #clear window from pictures
    window.clear()
    batch.draw()

def tick(dt):
    #funkce by mela zavolat tick() na kazdem objektu v objects 
    for obj in objects:
        obj.tick(dt)

def key_pressed(key, mod):
    pressed_keys.add(key)
    print(pressed_keys)

def key_released(key, mod):
    pressed_keys.discard(key)
    print(pressed_keys)


window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

window.push_handlers(
    on_draw = draw,
    on_key_press = key_pressed,
    on_key_release = key_released
)

pyglet.clock.schedule(tick)
objects.append(Spaceship(window))
pyglet.app.run()


### poznamky ###
"""
pyglet.graphics
pyglet.graphics.Batch()
pyglet.graphics.batch.draw()
batch
draw
pyglet - anchor
gl
set()
"""
