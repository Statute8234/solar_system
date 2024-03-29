import random

from ursina import *
move = True
time = 0
def update():
    global money,move,time
    # pause
    if move == True:
        # sun
        sun.rotation_y += 0.1
        # ring1
        for x in ring_list:
            x.rotation_y += x.speed
            x.rotation_x += 8
        # gain money
        time += 1
        if time == 10:
            if money > 7.50:
                money -= 7.50 * owen
        if time == 30:
            # random pay
            R = random.randint(0,1)
            if R == 0:
                money += 15 * owen
            time = 0
        # update text
        display_money.text = 'Money: ${:.2f}'.format(money)

    # update text
    display_money.text = 'Money: ${:.2f}'.format(money)
    # move camera
    if held_keys['x']:
        camera.rotation_z = 0
        camera.x = 0
        camera.z = -20
    if held_keys['e']:
        camera.rotation_z += 0.5
    if held_keys['q']:
        camera.rotation_z -= 0.5
    if held_keys['d']:
        camera.x += 0.5
    if held_keys['a']:
        camera.x -= 0.5
    if held_keys['w']:
        camera.z += 1
    if held_keys['s']:
        camera.z -= 1

app = Ursina()
sun = Entity(model = 'sphere',texture = 'download.jpg',scale = 2)
class Sphere(Button):
    def __init__(self, x, cost):
        super().__init__()
        self.parent = ring
        self.model = 'sphere'
        # random texture
        RT = random.randint(0,1)
        if RT == 0:
            self.texture = 'MoonMap2_2500x1250.jpg'
        else:
            self.texture = 'jSGZg.jpg'
        self.color = color.random_color()
        self.x = i - 20
        self.scale = random.uniform(0.01,0.9)
        self.highlight_color = color.red
        self.cost = cost
        self.click = True

    def input(self, key):
        global money, owen
        if self.hovered:
            if key == 'left mouse down':
                if self.click == True:
                    self.click = False
                    if money >= self.cost:
                        self.color = color.red
                        money -= self.cost
                        owen += 1

ring_list = []
for i in range(8):
    ring = Entity(model = 'quad',color = color.clear,speed = random.uniform(0.01,2))
    price = round(random.uniform(1,999),2)
    sphere = Sphere(x = i,cost = price)
    sphere.tooltip = Tooltip('name: {} \ncost ${:.2f}'.format('test',price))
    ring_list.append(ring)
# --------------------------------------------------------------- player
money = 499.50
owen = 0
bar = Entity(parent = camera.ui,model = 'quad',scale = (7,0.1),y = 0.45,color = color.black)
display_money = Text(text = 'Money: ${:.2f}'.format(money),y = 0.46,x = -0.8)
# pause button
press = 0
def Pause():
    global press,move
    if press % 2:
        press += 1
        pause.texture = 'pause (1).png'
        move = True
    else:
        press += 1
        pause.texture = 'texture/play-button.png'
        move = False
pause = Button(parent = camera.ui,model = 'quad',texture = 'pause (1).png',scale = (0.09,0.09),y = 0.35,x = 0.83,color = color.white)
pause.on_click = Pause
# sky
Sky(texture = 'seamless space_0.png')
app.run()
