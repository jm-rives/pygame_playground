#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# from the book "Instant Pygame for Python Game Development How-to" by Ivan Idris
# accessed at https://www.packtpub.com/mapt/book/game_development/9781782162865 July 31, 2018.
# critical modules for game funcition

import os, pygame
from pygame.locals import *

def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name)
    except(pygame.error, message):
        print("Cannot load image: ", name)

    image = image.convert()

    return image, image.get_rect()

class Head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('head.jpg', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.STEP = 9
        self.MARGIN = 12
        self.xstep = self.STEP
        self.ystep = 0
        self.degrees = 0
        self.direction = 'right'
        self.nhits = 0
        self.nmisses = 0

    def update(self):
        if self.degrees:
            self._spin()
        else:
            self._move()

    def _move(self):
        newpos = self.rect.move((self.xstep, self.ystep))

        if self.direction == 'right' and self.rect.right > self.area.right - self.MARGIN:
            self.xstep = 0
            self.ystep = self.STEP
            self.direction = 'down'

        if self.direction == 'down' and self.rect.bottom > self.area.bottom - self.MARGIN:
            self.xstep = -self.STEP
            self.ystep = 0
            self.direction = 'left'

        if self.direction == 'left' and self.rect.left < self.area.left + self.MARGIN:
            self.xstep = 0
            self.ystep = -self.STEP
            self.direction = 'up'

        if self.direction == 'up' and self.rect.top < self.area.top + self.MARGIN:
            self.xstep = self.STEP
            self.ystep = 0
            self.direction = 'right'

        self.rect = newpos

    def _spin(self):
        center = self.rect.center
        self.degrees = self.degrees + 12
        if self.degrees >= 360:
            self.degrees = 0
            self.image = self.original
        else:
            self.image = pygame.transform.rotate(self.original, self.degrees)
        self.rect = self.image.get_rect(center=center)

    def hit(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        collided = False
        bigger_rect = self.rect.inflate(40, 40)

        if bigger_rect.collidepoint(mouse_x, mouse_y):
            collided = True

        if not self.degrees and collided:
            self.degrees = 1
            self.original = self.image
            self.nhits += 1
        else:
            self.nmisses += 1



def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Collision Demo")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Hit the avatar!", 1, (0, 0, 200))
        textpos = text.get_rect(centerx = background.get_width()/2, centery = background.get_height()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    clock = pygame.time.Clock()
    head = Head()
    sprite = pygame.sprite.RenderPlain(head)

    while True:
        clock.tick(60)
        background.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()
        hammer, hammer_rect = load_image('hammer.png', -1)
        background.blit(hammer, mouse_pos)

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Hit the avatar!", 1, (0, 0, 200))
            textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/2)
            background.blit(text, textpos)

            text = font.render("Hits=%d" %(head.nhits), 1, (0, 200, 0))
            textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/2 + 36)
            background.blit(text, textpos)

            text = font.render("Misses=%d" %(head.nmisses), 1, (200, 0, 0))
            textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/2 + 72)
            background.blit(text, textpos)




        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == MOUSEBUTTONDOWN:
                head.hit()

        sprite.update()

        screen.blit(background, (0, 0))
        sprite.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
