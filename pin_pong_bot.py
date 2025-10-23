from pygame import *


win_h = 400
win_w = 700
window = display.set_mode((win_w, win_h))
display.set_caption('Pinpong')
game = True
finish = False
FPS = 60





class GameSprite(sprite.Sprite):
    def __init__(self,player_w, player_h, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.w = player_w
        self.h = player_h
        self.image = transform.scale(image.load(player_image), (self.w,self.h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def move(self,key1,key2):
        key_pressed = key.get_pressed()
        if key_pressed[key1] and self.rect.y >0:
            self.rect.y -= self.speed
        if key_pressed[key2] and self.rect.y < win_h-self.h:
            self.rect.y += self.speed
        
class Ball(GameSprite):
    def move(self):
        global speed_x
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y <= 0 or self.rect.y >= win_h-self.h:
            speed_y*= -1
        if sprite.collide_rect(self, racket1) or sprite.collide_rect(self, racket2):
            speed_x*= -1.1
            racket1.speed*=1.1
            racket2.speed*=1.1

class Bot(GameSprite):
    def move(self):
        self.rect.y += speed_y



background = transform.scale(image.load('background2.png'), (win_w,win_h))
racket1 = Racket(10,100,'пинпонг.png',130, 150, 3)
racket2 = Bot(10,100,'пинпонг.png',570, 150, 3)
ball = Ball(45,45,'Ball.png',170,175,3)
speed_x = ball.speed
speed_y = ball.speed
#ball = transform.scale(image.load('ball'), (100,90)) K_UP K_DOWN

clock = time.Clock()
while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))
        racket1.reset()
        racket1.move(K_w,K_s)
        racket2.reset()
        racket2.move()
        ball.reset()
        ball.move()
        #window.blit(ball,(200,100))


    display.update()
    clock.tick(FPS)