import pygame, sys
import random
from pygame.locals import *

#Declare globals and initiate pygame
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
HEIGHT = 600
WIDTH = 800
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ross Pong')
CLOCK = pygame.time.Clock()
FPS = 60



class Paddle(pygame.sprite.Sprite):
    def __init__(self, centery, centerx, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 60))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.speedy = 0
        self.player = player

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        #Paddle movement
        if self.player == 2:
            if keystate[pygame.K_UP]:
                self.speedy -= 5
            elif keystate[pygame.K_DOWN]:
                self.speedy += 5
            self.rect.y += self.speedy
        elif self.player == 1:
            if ball.speedx < 0:
                if ball.rect.centery == self.rect.centery:
                    self.speedy = 0
                elif ball.rect.centery > self.rect.centery:
                    self.speedy += 5
                elif ball.rect.centery < self.rect.centery:
                    self.speedy -= 5
            elif ball.speedx > 0:
                if self.rect.centery == HEIGHT/2:
                    self.speedy += 0
                elif self.rect.centery < HEIGHT/2:
                    self.speedy += 5
                elif self.rect.centery > HEIGHT/2:
                    self.speedy -= 5
            #Comment out above and use this instead if you want to play against another player.
            #if keystate[pygame.K_w]:
            #    self.speedy -= 5
            #if keystate[pygame.K_s]:
            #    self.speedy += 5
            self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.ballspeed = 2
        self.speedx = random.choice([2, -2])
        self.speedy = 2
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2

    def update(self):
        self.speedy = self.speedy
        self.speedx = self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy
        elif self.rect.bottom > HEIGHT:
            self.speedy = -self.speedy
        if pygame.sprite.collide_rect(self, paddle):
            self.speedx = -(self.speedx)
            self.speedx += .5
        elif pygame.sprite.collide_rect(self, paddle2):
            self.speedx = -(self.speedx)
            self.speedx -= .5
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            print('gg')
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = random.choice([2, -2])
        elif self.rect.left < 0:
            print('gg')
            self.rect.centerx = WIDTH/2
            self.rect.centery = HEIGHT/2
            self.speedx = random.choice([2, -2])

if __name__ == '__main__':
    #Create sprites group and add both our paddles and the ball
    all_sprites = pygame.sprite.Group()
    paddle = Paddle(HEIGHT/2, 10, 1)
    paddle2 = Paddle(HEIGHT/2, WIDTH - 10, 2)
    ball = Ball()
    all_sprites.add(paddle)
    all_sprites.add(paddle2)
    all_sprites.add(ball)

    #Game Loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        #Update sprites
        all_sprites.update()
        #Draw everything to the screen
        DISPLAY.fill(WHITE)
        all_sprites.draw(DISPLAY)
        pygame.display.flip()
        CLOCK.tick(FPS)
    pygame.quit()
    quit()
