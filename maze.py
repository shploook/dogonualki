#создай игру "Лабиринт"!
from pygame import *


window = display.set_mode((1000,800))
display.set_caption("trashkash")
background = transform.scale(image.load("background.jpg"), (1000,800))



class Gamer(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Hero(Gamer):
    def control(self):
        control = key.get_pressed()
        if control[K_w] and self.rect.y>0:
            self.rect.y -= Player.speed
        if control[K_s] and self.rect.y<600:
            self.rect.y += Player.speed
        if control[K_a] and self.rect.x>0:
            self.rect.x -= Player.speed
        if control[K_d] and self.rect.x<900:
            self.rect.x += Player.speed
class enemy(Gamer):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 900:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class wall(sprite.Sprite):
    def __init__(self, c1,c2,c3,wall_x,wall_y,wall_w,wall_h):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
       window.blit(self.image,(self.rect.x,self.rect.y)) 


Player = Hero('hero.png',100,100,10)
Villian = enemy('cyborg.png',600,400,10)
Theasure = Gamer('treasure.png', 850, 500, 0)
w1 = wall(154, 205, 50, 10, 10, 975, 10)
w2 = wall(154, 205, 50, 10, 10, 15, 700)
w3 = wall(154, 205, 50, 25, 675, 975, 10)
w4 = wall(154, 205, 50, 975, 10, 15, 700)



game = True
finish = False
clock = time.Clock()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
font.init()
font = font.SysFont(None,70)
win = font.render('YOU WIN', True,(255,215,0))
lose = font.render('YOU lose', True,(180,215,0))
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        Player.reset()
        Villian.reset()
        Theasure.reset()
        Player.control()
        Villian.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        if sprite.collide_rect(Player, Theasure):
            finish = True 
            window.blit(win, (400,350))
            money.play()
        if sprite.collide_rect(Player, Villian) or sprite.collide_rect(Player, w1) or sprite.collide_rect(Player, w2) or sprite.collide_rect(Player, w3) or sprite.collide_rect(Player,w4):
            finish = True 
            window.blit(lose, (400,350))
            kick.play()


    display.update()
    clock.tick(60)

