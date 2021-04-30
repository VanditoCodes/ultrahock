from p5 import *
import time
tiles = 40
tiles2 = 28
tile_size = 25
background_color = Color(250)
pause_overlay_color = Color(88, 127)
framerate = 240
w = 0
box_position = Vector(tile_size * 2, tile_size * 2)
box_position2 = Vector(tile_size * 38, tile_size * 26)
c1 = 50
c2 = 50
paused = False
l = []
class mapwalls:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size
    def makewall(self):
        fill(0)
        rect(self.pos, self.size[0], self.size[1])

class multi:
    def __init__(self, pos, size, acc):
        self.pos = pos
        self.size = 2
        self.acc = acc

def setup():
    w = 0
    size(tile_size * tiles, tile_size * (tiles2))
    title("GunSlinger")
    #outline
    l.append(mapwalls(Vector(0, 0), Vector(tile_size * tiles, 25)))
    l.append(mapwalls(Vector(0, 0), Vector(25, tile_size * tiles)))
    l.append(mapwalls(Vector(0, tile_size * (tiles2) - tile_size), Vector(tile_size * tiles, 25)))
    l.append(mapwalls(Vector(tile_size * tiles - tile_size, 0), Vector(25, tile_size * tiles)))

    #internal walls horizontal
    #w1
    l.append(mapwalls(Vector(0, tile_size * 7), Vector(tile_size * 9, tile_size)))
    #w2
    l.append(mapwalls(Vector(tile_size, tile_size * 10), Vector(tile_size, tile_size * 8)))
    l.append(mapwalls(Vector(tile_size * 2, tile_size * 10), Vector(tile_size, tile_size * 9)))
    l.append(mapwalls(Vector(tile_size * 3, tile_size * 10), Vector(tile_size, tile_size * 9)))
    l.append(mapwalls(Vector(tile_size * 4, tile_size * 10), Vector(tile_size, tile_size * 9)))
    l.append(mapwalls(Vector(tile_size * 5, tile_size * 10), Vector(tile_size, tile_size * 9)))
    l.append(mapwalls(Vector(tile_size * 6, tile_size * 10), Vector(tile_size, tile_size * 9)))
    l.append(mapwalls(Vector(0, tile_size * 18), Vector(tile_size * 5, tile_size)))
    #w3
    l.append(mapwalls(Vector(tile_size * 13, 0), Vector(tile_size, tile_size * 4)))
    #w4
    l.append(mapwalls(Vector(tile_size * 13, tile_size * 7), Vector(tile_size * 8, tile_size)))
    #w5
    l.append(mapwalls(Vector(tile_size * 13, tile_size * 8), Vector(tile_size, tile_size * 8)))
    #w6
    l.append(mapwalls(Vector(tile_size * 11, tile_size * 16), Vector(tile_size * 3, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 16), Vector(tile_size * 3, tile_size)))
    #w7
    l.append(mapwalls(Vector(tile_size * 9, tile_size * 25), Vector(tile_size * 1, tile_size * 2)))
    l.append(mapwalls(Vector(tile_size * 10, tile_size * 25), Vector(tile_size * 1, tile_size * 2)))
    #w8
    l.append(mapwalls(Vector(tile_size * 23, 0), Vector(tile_size, tile_size * 19)))
    #w9
    l.append(mapwalls(Vector(tile_size * 17, tile_size * 25), Vector(tile_size * 1, tile_size * 2)))
    l.append(mapwalls(Vector(tile_size * 18, tile_size * 25), Vector(tile_size * 1, tile_size * 2)))
    #w10
    l.append(mapwalls(Vector(tile_size * 26, tile_size * 3), Vector(tile_size, tile_size * 16)))
    #w11
    l.append(mapwalls(Vector(tile_size * 27, tile_size * 3), Vector(tile_size * 9, tile_size)))
    l.append(mapwalls(Vector(tile_size * 29, tile_size * 8), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 27, tile_size * 18), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 31, tile_size * 16), Vector(tile_size, tile_size * 5)))
    l.append(mapwalls(Vector(tile_size * 34, tile_size * 16), Vector(tile_size, tile_size * 5)))
    l.append(mapwalls(Vector(tile_size * 35, tile_size * 16), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 35, tile_size * 17), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 35, tile_size * 18), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 35, tile_size * 19), Vector(tile_size * 4, tile_size)))
    l.append(mapwalls(Vector(tile_size * 35, tile_size * 20), Vector(tile_size * 4, tile_size)))
    #W12
    l.append(mapwalls(Vector(tile_size * 26, tile_size * 26), Vector(tile_size * 1, tile_size)))
    l.append(mapwalls(Vector(tile_size * 27, tile_size * 26), Vector(tile_size * 1, tile_size)))
    l.append(mapwalls(Vector(tile_size * 28, tile_size * 26), Vector(tile_size * 1, tile_size)))
    l.append(mapwalls(Vector(tile_size * 29, tile_size * 26), Vector(tile_size * 1, tile_size)))
    l.append(mapwalls(Vector(tile_size * 30, tile_size * 26), Vector(tile_size * 1, tile_size)))
    l.append(mapwalls(Vector(tile_size * 31, tile_size * 26), Vector(tile_size * 1, tile_size)))
    no_stroke()

def draw():
    global paused
    global w
    background(background_color)

    if paused and w > 0:
        time.sleep(1)
        background(250)
        fill(0)
        if w == 1:
            text("BLACK WINS", ((tile_size * tiles)/2, (tile_size * (tiles - 6))/2))
        if w == 2:
            text("WHITE WINS", ((tile_size * tiles)/2, (tile_size * (tiles - 6))/2))
        return
    elif paused and w == 0:
        return

    for i in l:
        i.makewall()




    if key == "D":
        while not any(((box_position2.y <= i.size[1] and box_position2.y >= i.pos.y)or(box_position2.y <= i.pos.y + i.size[1] and box_position2.y >= i.pos.y)) and ((i.pos.x == box_position2.x) or (i.pos.x + (i.size[0] - tile_size) == box_position2.x)) for i in l):
            box_position2.x += 1
        else:
            box_position2.x -= 25
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "A":
        while not any(((box_position2.y <= i.size[1] and box_position2.y >= i.pos.y)or(box_position2.y <= i.pos.y + i.size[1] and box_position2.y >= i.pos.y)) and ((i.pos.x == box_position2.x) or (i.pos.x + (i.size[0] - tile_size) == box_position2.x)) for i in l):
            box_position2.x -= 1
        else:
            box_position2.x += 50
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "S":
        while not any(((box_position2.x <= i.size[0] and box_position2.x >= i.pos.x) or (box_position2.x <= i.pos.x + i.size[0] and box_position2.x >= i.pos.x)) and ((i.pos.y == box_position2.y) or (i.pos.y + (i.size[1] - tile_size) == box_position2.y)) for i in l):
            box_position2.y += 1
        else:
            box_position2.y -= 25
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "W":
        while not any(((box_position2.x <= i.size[0] and box_position2.x >= i.pos.x) or (box_position2.x <= i.pos.x + i.size[0] and box_position2.x >= i.pos.x)) and ((i.pos.y == box_position2.y) or (i.pos.y + (i.size[1] - tile_size) == box_position2.y)) for i in l):
            box_position2.y -= 1
        else:
            box_position2.y += 50
            if box_position == box_position2:
                paused = True
                w = 2


    if key == "RIGHT":
        while not any(((box_position.y <= i.size[1] and box_position.y >= i.pos.y)or(box_position.y <= i.pos.y + i.size[1] and box_position.y >= i.pos.y)) and ((i.pos.x == box_position.x) or (i.pos.x + (i.size[0] - tile_size) == box_position.x)) for i in l):
            box_position.x += 1
        else:
            box_position.x -= 25
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "LEFT":
        while not any(((box_position.y <= i.size[1] and box_position.y >= i.pos.y)or(box_position.y <= i.pos.y + i.size[1] and box_position.y >= i.pos.y)) and ((i.pos.x == box_position.x) or (i.pos.x + (i.size[0] - tile_size) == box_position.x)) for i in l):
            box_position.x -= 1
        else:
            box_position.x += 50
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "DOWN":
        while not any(((box_position.x <= i.size[0] and box_position.x >= i.pos.x) or (box_position.x <= i.pos.x + i.size[0] and box_position.x >= i.pos.x)) and ((i.pos.y == box_position.y) or (i.pos.y + (i.size[1] - tile_size) == box_position.y)) for i in l):
            box_position.y += 1
        else:
            box_position.y -= 25
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "UP":
        while not any(((box_position.x <= i.size[0] and box_position.x >= i.pos.x) or (box_position.x <= i.pos.x + i.size[0] and box_position.x >= i.pos.x)) and ((i.pos.y == box_position.y) or (i.pos.y + (i.size[1] - tile_size) == box_position.y)) for i in l):
            box_position.y -= 1
        else:
            box_position.y += 50
            if box_position == box_position2:
                paused = True
                w = 1

    #char1
    fill(100)
    circle(box_position2, tile_size * 2)
    #char2
    fill(0)
    circle(box_position, tile_size * 2)

    if key == "SPACE" and paused:
        paused = False
    elif key == "SPACE":
        paused = True
        return

    #temp
    '''for i in range(tiles):
        for j in range(tiles):
            fill(255)
            rect((tile_size * j, tile_size * i), 5, 5)'''

if __name__ == '__main__':
    run(frame_rate=framerate)
