from pygame_functions import *

class Sprite(object):
    # Should set up sprite images like this
    my_sprite_images = ["D1.png", "D2.png", "D3.png", "U1.png", "U2.png", "U3.png",
                        "L1.png", "L2.png", "L3.png", "L4.png", "L5.png", "L6.png",
                        "L7.png", "L8.png", "L9.png", "R1.png", "R2.png", "R3.png",
                        "R4.png", "R5.png", "R6.png", "R7.png", "R8.png", "R9.png"]

    def __init__(self, sprite_image, x = 0, y = 0):
        self.sprite_image = sprite_image
        self.x = x
        self.y = y
        self.speed = 5
        self.sprite = makeSprite(self.sprite_image)
        self.next_image = 0

        for i in self.my_sprite_images[1:24]:
            addSpriteImage(self.sprite, i)

    def walk(self):
        while True:
            if keyPressed('left'):
                self.x -= self.speed

                if self.next_image == 0:
                    self.next_image += 6
                elif 5 < self.next_image < 14:
                    self.next_image += 1
                else:
                    self.next_image = 7

            elif keyPressed('right'):
                self.x += self.speed

                if self.next_image == 0:
                    self.next_image += 15
                elif 14 < self.next_image < 23:
                    self.next_image += 1
                else:
                    self.next_image = 15

            elif keyPressed('up'):
                scrollBackground(0, 5)

                if self.next_image == 0:
                    self.next_image += 3
                elif 2 < self.next_image < 5:
                    self.next_image += 1
                else:
                    self.next_image = 3

            elif keyPressed('down'):
                scrollBackground(0, -5)

                if self.next_image < 2:
                    self.next_image += 1
                else:
                    self.next_image = 0

            else:
                self.next_image = 0

            changeSpriteImage(self.sprite, self.next_image)
            moveSprite(self.sprite, self.x, self.y, True)
            showSprite(self.sprite)

            tick(10)



screenSize(600, 600)
setBackgroundImage([['1.png'], ['2.png']])

my_sprite = Sprite(Sprite.my_sprite_images[0], 300, 300)
my_sprite.walk()
