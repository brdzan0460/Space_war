# Imports
import pygame
import random
# Initialize game engine
pygame.init()


# Window
WIDTH = 1800
HEIGHT = 1000
SIZE = (WIDTH, HEIGHT)
TITLE = "Aliens Suprise Attack"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)
score = 0

# Timer
clock = pygame.time.Clock()
refresh_rate = 15

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
WHITE_3 = (220, 239, 244)
WHITE_4 = (212, 240, 247)
WHITE_5 = (200, 237, 247)


# Fonts
FONT_SM = pygame.font.Font(None, 24)
FONT_MD = pygame.font.Font(None, 32)
FONT_LG = pygame.font.Font(None, 64)
FONT_XL = pygame.font.Font("assets/fonts/spacerangerboldital.ttf", 96)


# Images
ship_img = pygame.image.load('assets/images/player.png').convert_alpha()
enemy_img = pygame.image.load('assets/images/enemyShip.png').convert_alpha()
projectile1_img = pygame.image.load('assets/images/projectile-1.png.png').convert_alpha()
projectile2_img = pygame.image.load('assets/images/projectile-2.png.png').convert_alpha()
projectile3_img = pygame.image.load('assets/images/projectile-3.png.png').convert_alpha()
projectile4_img = pygame.image.load('assets/images/projectile-4.png.png').convert_alpha()
projectile5_img = pygame.image.load('assets/images/projectile-5.png.png').convert_alpha()
projectile6_img = pygame.image.load('assets/images/projectile-6.png.png').convert_alpha()
projectile7_img = pygame.image.load('assets/images/projectile-7.png.png').convert_alpha()
projectile8_img = pygame.image.load('assets/images/projectile-8.png.png').convert_alpha()
projectile9_img = pygame.image.load('assets/images/projectile-9.png.png').convert_alpha()
projectile10_img = pygame.image.load('assets/images/projectile-10.png.png').convert_alpha()
projectile11_img = pygame.image.load('assets/images/projectile-11.png.png').convert_alpha()
projectile12_img = pygame.image.load('assets/images/projectile-12.png.png').convert_alpha()
projectile13_img = pygame.image.load('assets/images/projectile-13.png.png').convert_alpha()
projectile14_img = pygame.image.load('assets/images/projectile-14.png.png').convert_alpha()
bomb1_img = pygame.image.load('assets/images/bomb-1.png.png').convert_alpha()
bomb2_img = pygame.image.load('assets/images/bomb-2.png.png').convert_alpha()
bomb3_img = pygame.image.load('assets/images/bomb-3.png.png').convert_alpha()
bomb4_img = pygame.image.load('assets/images/bomb-4.png.png').convert_alpha()
bomb5_img = pygame.image.load('assets/images/bomb-5.png.png').convert_alpha()
protagonist3_img = pygame.image.load('assets/images/Protagonist -1.png.png').convert_alpha()
protagonist4_img = pygame.image.load('assets/images/Protagonist -2.png.png').convert_alpha()
protagonist5_img = pygame.image.load('assets/images/Protagonist -3.png.png').convert_alpha()
protagonist1_img = pygame.image.load('assets/images/Protagonist -4.png.png').convert_alpha()
protagonist2_img = pygame.image.load('assets/images/Protagonist -5.png.png').convert_alpha()
ship_enemy1_img = pygame.image.load('assets/images/ship_enemy -1.png.png').convert_alpha()
ship_enemy2_img = pygame.image.load('assets/images/ship_enemy -2.png.png').convert_alpha()
ship_enemy3_img = pygame.image.load('assets/images/ship_enemy -3.png.png').convert_alpha()
health_boost1_img = pygame.image.load('assets/images/health-1.png.png').convert_alpha()
health_boost2_img = pygame.image.load('assets/images/health-2.png.png').convert_alpha()
ufo_img = pygame.image.load('assets/images/UFO-1.png.png').convert_alpha()

projectiles = [projectile1_img, projectile2_img, projectile3_img,projectile4_img, projectile5_img,
               projectile6_img, projectile7_img,
               projectile8_img, projectile9_img, projectile10_img, projectile11_img,
               projectile12_img, projectile13_img, projectile14_img]

bombs_animation = [bomb1_img, bomb2_img, bomb3_img, bomb4_img, bomb5_img]
protagonists = [protagonist1_img, protagonist2_img, protagonist3_img, protagonist4_img, protagonist5_img]
enemy_ships = [ship_enemy1_img, ship_enemy2_img, ship_enemy3_img]

health_animation = [health_boost1_img, health_boost2_img]

# Sounds
EXPLOSION = pygame.mixer.Sound('assets/sounds/explosion.ogg')
SHOOT = pygame.mixer.Sound('assets/sounds/attack.ogg')

# Stages
START = 0
PLAYING = 1
WIN = 2
LOSE = 3 


# Game classes
#################################################################
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

       
        self.image = protagonist1_img
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.ticks = 0
        self.rect.y = y
        self.speed = 12
        self.img_index = 0
        self.direct_cycle = True
        self.health = 5
        
    def move_left(self):
        self.rect.x -= self.speed
    
    def move_right(self):
        self.rect.x += self.speed

    def move_down(self):
        self.rect.y += self.speed
    
    def move_up(self):
        self.rect.y -= self.speed

    def shoot(self):
        #print ("PEW!")
        SHOOT.play()
        if len(lasers) < 5:
            laser = Laser(projectiles)
            laser.rect.centerx = self.rect.centerx 
            laser.rect.centery = self.rect.top
            lasers.add(laser) 

    def update(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.bottom < 0:
            self.rect.bottom = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

        if self.health == 4:

            self.image = protagonist2_img

        elif self.health == 3:

            self.image = protagonist3_img

        elif self.health == 2:

            self.image = protagonist4_img

        elif self.health == 1:

            self.image = protagonist5_img

        '''check powerups '''

        hit_list = pygame.sprite.spritecollide(self, powerups, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            print ("woot beep")
            hit.apply(self) 
            
        '''check bombs '''

        hit_list = pygame.sprite.spritecollide(self, bombs, True, pygame.sprite.collide_mask)

        for hit in hit_list:
            print("oof!")
            self.health -= 1

        if self.health <= 0:
            self.kill() 
            
   
#################################################################
class Laser(pygame.sprite.Sprite):
    def __init__(self, projectiles):
        super().__init__()

        
        
        self.images = projectiles
        self.image = projectiles[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speed = 10
        self.ticks = 0
        self.img_index = 0
        self.direct_cycle = True
        
    def update(self):
        
        self.ticks += 1
        
        if self.ticks %2 == 0:
            if self.direct_cycle:
                self.img_index += 1
                if self.img_index == 14:
                    self.direct_cycle = not self.direct_cycle
                    
            if not self.direct_cycle:
                self.img_index -= 1
                if self.img_index == 0:
                    self.direct_cycle = not self.direct_cycle
            
            self.image = self.images[self.img_index]
            
        self.rect.y -= self.speed
        if self.rect.top < 0:
            #self.speed += 1
            self.speed  *= -1
            #print(self.speed)

        elif self.rect.bottom > HEIGHT:
            #self.speed -= 1
            self.speed *= -1
            #print(self.speed)
            
#################################################################
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.images = enemy_ships 
        self.image = enemy_ships[0]
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.ticks = 0
        self.rect.y = y
        self.speed = 12
        self.img_index = 0
        self.direct_cycle = True

    def drop_bomb(self):
        print ("bwampwrino!")
        bomb = Bomb(bombs_animation)
        bomb.rect.centerx = self.rect.centerx 
        bomb.rect.centery = self.rect.bottom 
        bombs.add(bomb) 

    def update(self):
        global score
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        
        if len(hit_list) > 0:
            #print("Boom!")
            self.kill()
            score += 1
        

        self.ticks += 1
        
        if self.ticks %2 == 0:
            if self.direct_cycle:
                self.img_index += 1
                if self.img_index == 3:
                    self.direct_cycle = not self.direct_cycle
                    
            if not self.direct_cycle:
                self.img_index -= 1
                if self.img_index == 0:
                    self.direct_cycle = not self.direct_cycle
            
            self.image = self.images[self.img_index]
#################################################################
class Bomb(pygame.sprite.Sprite):
    def __init__(self, bombs_animation):
        super().__init__()

        
        
        self.images = bombs_animation
        self.image = bombs_animation[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speed = -10
        self.ticks = 0
        self.img_index = 0
        self.direct_cycle = True
        
    def update(self):
        
        self.ticks += 1
        
        if self.ticks %15 == 0:
            if self.direct_cycle:
                self.img_index += 1
                if self.img_index == 5:
                    self.direct_cycle = not self.direct_cycle
                    
            if not self.direct_cycle:
                self.img_index -= 1
                if self.img_index == 0:
                    self.direct_cycle = not self.direct_cycle
            
            self.image = self.images[self.img_index]
            
        self.rect.y -= self.speed
        if self.rect.top < 0:
            #self.speed += 1
            self.speed  *= -1
            #print(self.speed)

        elif self.rect.bottom > HEIGHT:
            #self.speed -= 1
            self.speed *= -1
            #print(self.speed)
        

#################################################################
class HealthPowerUp(pygame.sprite.Sprite):
    
    def __init__(self, x, y, health_animation):
        super().__init__()

        self.images = health_animation
        self.image = health_animation[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.ticks = 0
        self.img_index = 0
        self.direct_cycle = True

    def apply(self,ship):
        ship.health = 5
        ship.image = protagonist1_img

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > HEIGHT:
            self.kill()

        self.ticks += 1
    
        if self.ticks %15 == 0:
            if self.direct_cycle:
                self.img_index += 1
                if self.img_index == 2:
                    self.direct_cycle = not self.direct_cycle
                    
            if not self.direct_cycle:
                self.img_index -= 1
                if self.img_index == 0:
                    self.direct_cycle = not self.direct_cycle
            
            self.image = self.images[self.img_index]

#################################################################
class Fleet():
    
    def __init__(self, mobs):
        self.mobs = mobs
        self.speed = 5
        self.drop = 20
        self.moving_right = True
        self.bomb_speed = 20
        self.bomb_rate = 12
        #lover is faster
        

    def move(self):
        hits_edge = False

        for m in mobs:
            if self.moving_right:
                m.rect.x += self.speed

                if m.rect.right >= WIDTH:
                    hits_edge = True

            else:
                m.rect.x -= self.speed

                if m.rect.left <= 0:
                    hits_edge = True

        if hits_edge :
            self.reverse()
            #self.move_down()
    
    def reverse(self):
        self.moving_right = not self.moving_right

    def move_down(self):
        for m in mobs:
            m.rect.y += self.drop

    def choose_bomber(self):
        rand = random.randrange(self.bomb_rate)
        mob_list = mobs.sprites()

        if len(mob_list) > 0 and rand ==0:
            bomber = random.choice(mob_list)
            bomber.drop_bomb()
            
    def update(self):
        self.move()
        self.choose_bomber()

#################################################################
class UFO(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()

        self.image = ufo_img
        self.rect = image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.ticks = 0
        self.rect.y = y
        self.speed = 24
    
 

    def update(self):
        global score
        hit_list = pygame.sprite.spritecollide(self, lasers, True, pygame.sprite.collide_mask)
        self.rect.x += self.speed
        if len(hit_list) > 0:
            #print("Boom!")
            self.kill()
            score += 30
        
  
             
#################################################################
# Game helper functions
def show_title_screen():

    title_text = FONT_XL.render("Space War!", 1, WHITE)
    start_text = FONT_XL.render("Press Space!", 1, WHITE)
    s = start_text.get_width()
    t = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 -  t/2, 400))
    screen.blit(start_text, (WIDTH/2 -  s/2, 450))

def show_win_screen():
    
    title_text = FONT_XL.render("WINNER!", 1, WHITE)
    start_text = FONT_XL.render("Press R to reset!", 1, WHITE)
    s = start_text.get_width()
    t = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 -  t/2, 400))
    screen.blit(start_text, (WIDTH/2 -  s/2, 450))

def show_lose_screen():

    title_text = FONT_XL.render("LOOSER!", 1, WHITE)
    start_text = FONT_XL.render("Press R to reset!", 1, WHITE)
    s = start_text.get_width()
    t = title_text.get_width()
    screen.blit(title_text, (WIDTH/2 -  t/2, 400))
    screen.blit(start_text, (WIDTH/2 -  s/2, 450))
    
def show_stats(player):
    health_show = FONT_XL.render(str(ship.health), 1, WHITE)
    screen.blit(health_show, [50, 50])
    score_text = FONT_XL.render(str(score), 1, WHITE)
    screen.blit(score_text, [WIDTH - 200, 50])


def check_end():
    global stage
    global score
    if len(mobs) == 0:
        setup()
        score += 10

    elif len(mobs) == 0 and len(player) == 5:
        stage = WIN 
        

    elif len(player) == 0:
        stage = LOSE 

def setup():
    global stage, done, player, protagonists, enemy_ship, ufos
    global ship, lasers, mobs, fleet, bombs, powerups, score


   
    ''' Make game objects '''
    ship =Ship(900, 950, ship_img)
    ship.rect.centerx = WIDTH /2
    ship.rect.bottom = HEIGHT - 150

    ufo = UFO(-2000, 50, ufo_img)

    ''' Make sprite groups '''
    player = pygame.sprite.GroupSingle()
    player.add(ship)
    lasers = pygame.sprite.Group()
    bombs = pygame.sprite.Group()

    mob1 = Mob(200,100, enemy_img)
    mob2 = Mob(400,100, enemy_img)
    mob3 = Mob(600,100, enemy_img)
    mob4 = Mob(800,100, enemy_img)
    mob5 = Mob(1000,100, enemy_img)
    mob6 = Mob(1200,100, enemy_img)
    mob7 = Mob(1400,100, enemy_img)
    mob8 = Mob(1600,100, enemy_img)
    mob9 = Mob(200,200, enemy_img)
    mob10 = Mob(200,200, enemy_img)
    mob11 = Mob(400,200, enemy_img)
    mob12 = Mob(600,200, enemy_img)
    mob13 = Mob(800,200, enemy_img)
    mob14 = Mob(1000,200, enemy_img)
    mob15 = Mob(1200,200, enemy_img)
    mob16 = Mob(1400,200, enemy_img)
    mob17 = Mob(1600,200, enemy_img)
    mob18 = Mob(200,300, enemy_img)
    mob19 = Mob(400,300, enemy_img)
    mob20 = Mob(600,300, enemy_img)
    mob21 = Mob(800,300, enemy_img)
    mob22 = Mob(1000,300, enemy_img)
    mob23 = Mob(1200,300, enemy_img)
    mob24 = Mob(1400,300, enemy_img)
    mob25 = Mob(1600,300, enemy_img)

    

    
    ufos = pygame.sprite.Group()
    ufos.add(ufo)
    mobs = pygame.sprite.Group()
    mobs.add(mob1,mob2, mob3, mob4, mob5, mob6, mob7, mob8, mob9, mob10, mob11,
             mob12, mob13, mob14, mob15, mob16, mob17,
             mob18, mob19, mob20, mob21, mob22, mob23, mob24, mob25 ) 

    powerup1 = HealthPowerUp(900, -2000 , health_animation)
    powerups = pygame.sprite.Group()
    powerups.add(powerup1) 

    
    fleet = Fleet(mobs)
    
    
    
    ''' set stage '''
    stage = START
    done = False

    
    
def draw_stars_3():
    
    stars = []
    for i in range(500 ):
        x = random.randrange(0, 1800)
        y = random.randrange(0 , 1000)
        d = random.randrange(1, 10) 
        s = [ x ,y, d, d]
        stars.append(s)
    for s in stars:
        pygame.draw.rect(screen, WHITE_4, s)
        
def draw_stars_4 ():
    
    stars = []
    for i in range(500 ):
        x = random.randrange(0, 1800)
        y = random.randrange(0 , 1000)
        d = random.randrange(1, 10) 
        s = [ x ,y, d, d]
        stars.append(s)
    for s in stars:
        pygame.draw.rect(screen, WHITE_4, s)

def draw_stars_5 ():
    
    stars = []
    for i in range(500 ):
        x = random.randrange(0, 1800)
        y = random.randrange(0 , 1000)
        d = random.randrange(1, 10) 
        s = [ x ,y, d, d]
        stars.append(s)
    for s in stars:
        pygame.draw.rect(screen, WHITE_4, s)

def draw_background():
    screen.fill(BLACK)
    draw_stars_3()
    draw_stars_4()
    draw_stars_5()

pygame.mixer.music.load("assets/sounds/music.ogg")
pygame.mixer.music.play(-1) 

    
# Game loop
setup()

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif stage == START:
                if event.key == pygame.K_SPACE:
                    refresh_rate = 30
                    stage = PLAYING
            elif stage == PLAYING:
                if event.key == pygame.K_SPACE:
                    ship.shoot()

                elif event.key == pygame.K_t:
                    refresh_rate = 60

            elif stage == LOSE:
                if event.key == pygame.K_r:
                    setup()
            elif stage == WIN:
                if event.key == pygame.K_r:
                    setup()
            

    pressed = pygame.key.get_pressed()
        
    
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING :
        if pressed[pygame.K_LEFT]:
           ship.move_left()
        elif pressed[pygame.K_RIGHT]:
            ship.move_right()
        elif pressed[pygame.K_DOWN]:
           ship.move_down()
        elif pressed[pygame.K_UP]:
            ship.move_up()

               
        player.update()
        lasers.update()
        bombs.update()
        fleet.update()
        mobs.update()
        powerups.update()
        check_end()
        ufos.update()

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    draw_background()
    lasers.draw(screen)
    player.draw(screen)
    bombs.draw(screen)
    mobs.draw(screen)
    powerups.draw(screen)
    show_stats(player) 
    ufos.draw(screen)

    
    if stage == START:
        show_title_screen()

    elif stage == WIN:
        show_win_screen()

    elif stage == LOSE:
        show_lose_screen()  

        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
