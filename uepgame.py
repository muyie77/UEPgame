from pygame_functions import *
from random import randint

screenSize(600, 600)
setBackgroundImage([['1.png'], ['2.png']])
setAutoUpdate(False)

quips = ["Hain daw la a <br> mga tawo sa UEP?",
         "Kamingaw daw sa <br> lane yana.",
         "May bomb threat <br> ada yana sa <br> UEP kaya waray tawo.",
         "May bagyo ba? Nanu <br> daw kay wa klase?"
         "Kun san.o man ak <br> nasulod mao man wa klase.",
         "Sayang la ak <br> plantsado nga uniform."]

main_sprite = ["L1.png", "L2.png", "L3.png", "L4.png", "L5.png", "L6.png",
               "L7.png", "L8.png", "L9.png", "R1.png", "R2.png", "R3.png",
               "R4.png", "R5.png", "R6.png", "R7.png", "R8.png", "R9.png",
               "D1.png", "D2.png", "D3.png", "U1.png", "U2.png", "U3.png"]
x = 200
y = 300
speed = 5
next_image = 0
time = 0
statement = 0

my_sprite = makeSprite(main_sprite[18])
aw = makeLabel(quips[statement], 24, x - 100, 200, background = 'white')

for i in main_sprite[0:24]:
    addSpriteImage(my_sprite, i)

# Blocking, collisions
#def check_collision(sprite, object):
#    if touching(sprite, object):
#        pass

# Walking
while True:
    time += 1

    if time == 100:
        hideLabel(aw)
        statement += 1
        changeLabel(aw, quips[statement])
        time = 0
    elif time == 50:
        showLabel(aw)

    if keyPressed('left'):
        x -= speed

        if next_image < 9:
            next_image += 1
        else:
            next_image = 1
    elif keyPressed('right'):
        x += speed

        if 9 < next_image < 18:
            next_image += 1
        else:
            next_image = 10
    elif keyPressed('up'):
        scrollBackground(0, 5)

        if 21 < next_image < 24:
            next_image += 1
        else:
            next_image = 22
    elif keyPressed('down'):
        scrollBackground(0, -5)

        if 19 < next_image < 21:
            next_image += 1
        else:
            next_image = 20
    else:
        next_image = 0

# If reaches the edge of the screen (left or right), shows up on the opposite edge
    if x < 0:
        x = 600
    elif x > 600:
        x = 0
    else:
        pass

    changeSpriteImage(my_sprite, next_image)
    moveSprite(my_sprite, x, y, True)
    showSprite(my_sprite)
    updateDisplay()

    tick(10)
