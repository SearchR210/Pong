from pygame import *
from time import time as timer

win_x = 500
win_y = 500
window = display.set_mode((win_x,win_y))
col1 = (255, 255, 255)
window.fill(col1)
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None, 40)
lose1 = font1.render('PLAYER 1 LOSE!', True, (0, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (0, 0, 0))

font2 = font.Font(None, 36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_y - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_y - 80:
            self.rect.y += self.speed


ball = GameSprite('ball.png', 225, 225, 4, 50, 50)
racket_r = Player('racket.png', 30, 200, 4, 50, 150)
racket_l = Player('racket.png', 420, 200, 4, 50, 150)
start_time = timer()

run = True
finish = False
while run:
    new_time = timer()
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(col1)
        racket_l.update_l()
        racket_r.update_r()
        if float(new_time - start_time) > 1.5:
            ball.rect.x += speed_x
            ball.rect.y += speed_y

        if sprite.collide_rect(racket_r, ball) or sprite.collide_rect(racket_l, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_y - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_x:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        ball.reset()
        racket_r.reset()
        racket_l.reset()
        display.update()
    clock.tick(FPS)

display.update()

