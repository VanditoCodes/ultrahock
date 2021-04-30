from p5 import *
import time
tiles = 25
tile_size = 25
background_color = Color(250)
pause_overlay_color = Color(88, 127)
framerate = 240
w = 0
box_position = Vector(tile_size * 2, tile_size * 2)
box_position2 = Vector(tile_size * 11, tile_size * 13)
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
    size(tile_size * tiles, tile_size * (tiles - 6))
    title("GunSlinger")
    #outline
    l.append(mapwalls(Vector(0, 0), Vector(tile_size * tiles, 25)))
    l.append(mapwalls(Vector(0, 0), Vector(25, tile_size * tiles)))
    l.append(mapwalls(Vector(0, tile_size * (tiles - 6) - tile_size), Vector(tile_size * tiles, 25)))
    l.append(mapwalls(Vector(tile_size * tiles - tile_size, 0), Vector(25, tile_size * tiles)))

    #internal walls horizontal
    l.append(mapwalls(Vector(0, tile_size * 3), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(0, tile_size * 3), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(0, tile_size * 3), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(0, tile_size * 3), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(0, tile_size * 3), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 3), Vector(tile_size * 5, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 4), Vector(tile_size * 5, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 5), Vector(tile_size * 5, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 6), Vector(tile_size * 5, tile_size)))
    l.append(mapwalls(Vector(tile_size * 16, tile_size * 7), Vector(tile_size * 5, tile_size)))
    l.append(mapwalls(Vector(0, tile_size * 11), Vector(tile_size * 13, tile_size)))
    l.append(mapwalls(Vector(tile_size * 12, tile_size * 12), Vector(tile_size, tile_size)))
    l.append(mapwalls(Vector(tile_size * 12, tile_size * 13), Vector(tile_size, tile_size)))
    l.append(mapwalls(Vector(tile_size * 12, tile_size * 14), Vector(tile_size, tile_size)))
    l.append(mapwalls(Vector(tile_size * 21, tile_size * 15), Vector(tile_size * 3, tile_size)))
    l.append(mapwalls(Vector(tile_size * 21, tile_size * 16), Vector(tile_size * 3, tile_size)))
    l.append(mapwalls(Vector(tile_size * 21, tile_size * 17), Vector(tile_size * 3, tile_size)))
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
        while not any(((box_position2.y <= i.size[1] and box_position2.y >= i.pos.y)or(box_position2.y <= i.pos.y + i.size[1] and box_position2.y >= i.pos.y)) and (i.pos.x == box_position2.x) for i in l):
            box_position2.x += 1
        else:
            box_position2.x -= 25
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "A":
        while not any(((box_position2.y <= i.size[1] and box_position2.y >= i.pos.y)or(box_position2.y <= i.pos.y + i.size[1] and box_position2.y >= i.pos.y)) and (i.pos.x == box_position2.x) for i in l):
            box_position2.x -= 1
        else:
            box_position2.x += 50
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "S":
        while not any(((box_position2.x <= i.size[0] and box_position2.x >= i.pos.x) or (box_position2.x <= i.pos.x + i.size[0] and box_position2.x >= i.pos.x)) and (i.pos.y == box_position2.y) for i in l):
            box_position2.y += 1
        else:
            box_position2.y -= 25
            if box_position == box_position2:
                paused = True
                w = 2

    elif key == "W":
        while not any(((box_position2.x <= i.size[0] and box_position2.x >= i.pos.x) or (box_position2.x <= i.pos.x + i.size[0] and box_position2.x >= i.pos.x)) and (i.pos.y == box_position2.y) for i in l):
            box_position2.y -= 1
        else:
            box_position2.y += 50
            if box_position == box_position2:
                paused = True
                w = 2


    if key == "RIGHT":
        while not any(((box_position.y <= i.size[1] and box_position.y >= i.pos.y)or(box_position.y <= i.pos.y + i.size[1] and box_position.y >= i.pos.y)) and (i.pos.x == box_position.x) for i in l):
            box_position.x += 1
        else:
            box_position.x -= 25
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "LEFT":
        while not any(((box_position.y <= i.size[1] and box_position.y >= i.pos.y)or(box_position.y <= i.pos.y + i.size[1] and box_position.y >= i.pos.y)) and (i.pos.x == box_position.x) for i in l):
            box_position.x -= 1
        else:
            box_position.x += 50
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "DOWN":
        while not any(((box_position.x <= i.size[0] and box_position.x >= i.pos.x) or (box_position.x <= i.pos.x + i.size[0] and box_position.x >= i.pos.x)) and (i.pos.y == box_position.y) for i in l):
            box_position.y += 1
        else:
            box_position.y -= 25
            if box_position == box_position2:
                paused = True
                w = 1

    elif key == "UP":
        while not any(((box_position.x <= i.size[0] and box_position.x >= i.pos.x) or (box_position.x <= i.pos.x + i.size[0] and box_position.x >= i.pos.x)) and (i.pos.y == box_position.y) for i in l):
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
