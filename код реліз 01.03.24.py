from pygame import *

init()
back = (200, 255, 255)
win_width = 1024
win_height = 512
window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y



    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self):
        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x :
            self.rect.x += self.speed
            
    def fire(self):
        keys_pressed = key.get_pressed()

        bullet = Bullet('pulae.png',self.rect.centerx+30,self.rect.top + 20,15,20,10,0)
        bullets.add(bullet)
        if keys_pressed[K_w]:
            self.fire()
    def check_collisions_down(self, blocks):
        is_on_ground = False
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if self.rect.bottom >= block.rect.top and self.rect.bottom <= block.rect.bottom:
                    self.rect.bottom = block.rect.top+30
                    is_on_ground = True
        if not is_on_ground:
            self.rect.y += 5

class Assasin(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
class Enemy(GameSprite): 
    def update(self): 
        self.rect.x -= self.speed 
       
    def fire(self):
        keys_pressed = key.get_pressed()

        bullet = Bullet('pulae.png',self.rect.centerx+30,self.rect.top + 20,15,20,10,0)
        bullets.add(bullet)
        if keys_pressed[K_w]:
            self.fire()

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x <0 :
            self.kill()
FPS = 40
bg_1 = transform.scale(image.load("fon4.jpg"), (win_width, win_height))
bg_2 = transform.scale(image.load("fon3.jpg"), (win_width, win_height))
bg_3 = transform.scale(image.load("level3.png"), (win_width, win_height))
bg_4 = transform.scale(image.load("photo1712252328.jpeg"), (win_width, win_height))
bg_5 = transform.scale(image.load("fon5.png"), (win_width, win_height))
display.set_caption("DARK FANTASY")
# font.init()
# font = font.Font(None, 65)
# txt = font("HELLO PLAYER")


clock = time.Clock()
level_4 =False
level_1 =False
level_1 =True
level_3 =False
level_5 =False

font.init()
font = font.Font(None, 65)
txt = font.render("YOU WIN", True, (232, 78, 67))
txt = font.render("YOU WIN", True, (232, 78, 67))

assasin_health = 50

jump_count =9
jump_height =9
jumping = False
run = True
player = Player('knight.png', 10, 350, 85, 100, 30)

assasins = sprite.Group()

assasin = Assasin('assasin.png',20,20,125,130,40)
assasins.add(assasin)

assasin1 = Assasin('assasin.png',820,20,125,130,27)
assasins.add(assasin1)

assasin1 = Assasin('assasin.png',420,20,125,130,35)
assasins.add(assasin1)

stars =  sprite.Group()
one_star = False
two_star = False


star_level = Player("star.png",810,300,40,40,0)
stars.add(star_level)


rocks = sprite.Group()

rock_1 = Assasin("rock.webp",30,300,150,100,14)
rocks.add(rock_1)
rock_2 = Assasin("rock.webp",260,200,150,100,34)
rocks.add(rock_2)
rock_3 = Assasin("rock.webp",470,100,150,100,20)
rocks.add(rock_3)

chests = sprite.Group()
chest = Enemy('chest2.png',260,362,250,250,34)
chests.add(chest)
# rock_4 = Assasin("rock.webp",100,50,40,40,30)
# rocks.add(rock_2)
# rock_5 = Assasin("rock.webp",150,50,40,40,18)
player_x = 50
player_y = 452
rocks.add(rock_2)
while run:
    time.delay(30)
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            run = False
    if level_1:
        window.blit(bg_1,(0,0))
        txt_start = font.render("To start the game you need to reach the end", True, (232, 78, 67))

        window.blit(txt_start,(70,100))

        if player.rect.x > win_width-80:
            level_2 = True
            level_1 = False
            player.rect.x = 400
            player.rect.x = 25
    elif level_2:
        window.blit(bg_2,(0,0))
        txt_start = font.render(f"{assasin_health}", True, (232, 78, 67))
        window.blit(txt_start,(10,10))

        assasin.reset()
        assasins.draw(window)
        stars.draw(window)
        for assasin in assasins:
            assasin.update()

        if player.rect.x <0:
            player.rect.x = 10
        
        if player.rect.x > win_width-70 :
    
            player.rect.x = win_width-70
        for assasin in assasins:
            if not (0 < assasin.rect.y < 380):
                assasin.speed *= -1
        if sprite.spritecollide(player, assasins, False):
                assasin_health -=1
                
        if assasin_health <= 0:
            level_1 =True
            level_2 =False
            level_3 =False
            assasin_health = 10
            
        if sprite.spritecollide(player, stars, True):
                one_star = True
                level_3 = True
                level_2 = False
                
    elif level_3:
        star_level = Player("star.png",780,100,40,40,0)
        stars.add(star_level)

        star_level.rect.x = 780
        star_level.rect.y = 100
   

        window.blit(bg_3,(0,0))
        stars.draw(window)
        rocks.draw(window)
        player.check_collisions_down(rocks)
        if  player.rect.bottom > 500:
            player.rect.bottom = 500
        if sprite.spritecollide(player, stars, True) :
            two_star = True
            one_star = False
            level_4 = True
            level_3 = False
            player.rect.x = 100
            player.rect.y= 300

    elif level_4:
        window.blit(bg_4,(0,0))
        chests.draw(window)
        if player.rect.y >500:
            player.rect.y = 300

            txt_win = font.render("You Win", True, (0, 225, 0))
            window.blit(txt_win,(200,200))
            





 

    elif level_5:
        window.blit(bg_5,(0,0))



    if not jumping:
        if keys[K_SPACE]:
            jumping = True

    else:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1
            player.rect.y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = jump_height
            
    if one_star:
        window.blit(transform.scale(image.load("star.png"),(30,30)),(win_width-40,10))
        
    if two_star:
        window.blit(transform.scale(image.load("star.png"),(30,30)),(win_width-40,10))
        window.blit(transform.scale(image.load("star.png"),(30,30)),(win_width-80,10))

    player.update()
    player.reset()
    
    if player.rect.x <0:
            player.rect.x = 23
        
    if player.rect.x > win_width-70 :
    
            player.rect.x = win_width-70


        
    display.update()

    time.delay(FPS)
