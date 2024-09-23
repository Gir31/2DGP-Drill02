from pico2d import *
import math

def character_triangle_move():
    grass = load_image('grass.png')
    character = load_image('character.png')
    x = 200
    y = 90
    while (x < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 2
        delay(0.001)
    while(y < math.sin(60/360*2*math.pi)*500):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y += 3**(1/2)
        x -= 1
        delay(0.001)
    while(y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 3**(1/2)
        x -= 1
        delay(0.001)

def character_circle_move():
    grass = load_image('grass.png')
    character = load_image('character.png')
    x = 400
    y = 90
    r = 360
    while (r > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= math.sin(r/360*2*math.pi) * 4
        x += math.cos(r/360*2*math.pi) * 4
        r -= 1
        delay(0.01)
    
        
    
open_canvas()

while (True):
    character_circle_move()
    character_triangle_move()

close_canvas()
