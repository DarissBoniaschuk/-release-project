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
        



FPS = 40
bg_1 = transform.scale(image.load("fon4.jpg"), (win_width, win_height))
display.set_caption("DARK FANTASY")

clock = time.Clock()
level_1 =True
level_1 =False
level_1 =False

jump_count =8
jump_height =8
jumping = False
run = True
player = Player('knight.png', 10, 350, 85, 100, 10)

while run:
    time.delay(30)
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(bg_1,(0,0))
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

    player.update()
    player.reset()


        
    display.update()

    time.delay(FPS)